import pandas as pd

f_save = "data/collated_header_cleaned_dataset.csv"


n_gram = 4

# Starting text to remove, found by inspection from running this code for various n-grams

filtered_lines = [
    "? ",
    "[unreadable] ",
    "description (adapted from applicant's abstract):",
    "description (adapted from applicant's abstract)",
    "description (provided by applicant):",
    "description (provided by applicant)",
    "description (provided by the applicant):",
    "description (provided by the applicant)",
    "description: (provided by applicant)",
    "description (adapted from the applicant's abstract):",
    "description: (adapted from the investigator's abstract)",
    "description: (adapted from the applicant's abstract)",
    "description: (adapted from the investigator's abstract)",
    "description: (adapted from investigator's abstract)",
    "description: (adapted from applicant's abstract)",
    "description (adapted from investigator's abstract):",
    "description (adapted from the investigator's abstract):",
    "description (adapted from the applicant's abstract)",
    "project summary / abstract",
    "project summary (see instructions):",
]

# Filter the actual header data here
df = pd.read_csv("data/collated_raw_dataset.csv")

for line in filtered_lines:
    idx = df["ABSTRACT_TEXT"].str.lower().str.startswith(line)
    df.loc[idx, "ABSTRACT_TEXT"] = (
        df.loc[idx, "ABSTRACT_TEXT"].str[len(line) :].str.strip()
    )
    print(line, idx.sum())

# Uncomment to see what's left (v. memory intensive!)
# df['header'] = df.ABSTRACT_TEXT.str.split().str[:n_gram].str.join(' ').str.lower()
# print()
# print(df.header.value_counts()[:20])

# Save what's left
df.to_csv(f_save, index=False)
