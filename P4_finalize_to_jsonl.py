import pandas as pd
import jsonlines
from tqdm import tqdm

chunks = pd.read_csv(
    "data/collated_header_cleaned_dataset.csv", chunksize=25000, nrows=None,
)


def data_iter():

    for df in chunks:
        for _, row in df.iterrows():
            item = {
                "meta": {"APPLICATION_ID": row["APPLICATION_ID"]},
                "text": row["ABSTRACT_TEXT"],
            }

            if not isinstance(item['text'], str):
                continue
            
            yield item


f_save = "data/NIH_ExPORTER_awarded_grant_text.jsonl"

with jsonlines.open(f_save, "w") as FOUT:
    FOUT.write_all(tqdm(data_iter()))
