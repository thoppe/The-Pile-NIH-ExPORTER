from dspipe import Pipe
import pandas as pd
from zipfile import ZipFile
from io import StringIO
from wasabi import msg

"""
There are a small number of (very bad) unicode erros baked into the data
that make it annoying to parse.
"""


def collate(f0):
    print(f0)

    # Unzip the file, look for the only file zipped
    # Read the file while ignoring errors
    with ZipFile(f0) as zf:
        for f_csv in zf.namelist():
            with zf.open(f_csv, "r") as FIN:
                content = FIN.read().decode(errors="ignore")

    # Convert the string into a dataframe
    df = pd.read_csv(StringIO(content))

    # Drop entries without text
    idx = df["ABSTRACT_TEXT"].isnull()
    df = df[~idx]

    # Clean the text a bit
    df["ABSTRACT_TEXT"] = df["ABSTRACT_TEXT"].astype(str).str.strip()

    df["ABSTRACT_TEXT"] = df["ABSTRACT_TEXT"].str.split().str.join(" ")

    return df


P = Pipe("data/CSV", input_suffix=".zip", shuffle=True, limit=None)

df = pd.concat(P(collate, -1))
msg.good(f"{len(df):,} applications read in")

# Keep only one copy for each applID,
# may happen since we are mixing RePORTER and CRISP
df = df.drop_duplicates(subset=["APPLICATION_ID"])
msg.good(f"{len(df):,} applications after filtering for dupe applID")

# Some early projects repeat text or are only biolerplate
# Drop them at this step
df = df.drop_duplicates(subset=["ABSTRACT_TEXT"])
msg.good(f"{len(df):,} applications after filtering for dupe text")

# Set index on the applID
df = df.set_index("APPLICATION_ID").sort_index()

df.to_csv("data/collated_raw_dataset.csv")
