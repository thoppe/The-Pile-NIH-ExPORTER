# The-Pile-NIH-ExPORTER

Download, parse, and filter NIH-awarded grant data from [ExPORTER](https://exporter.nih.gov/), data-ready for [The-Pile](https://github.com/EleutherAI/The-Pile).

Data is pulled from both RePORTER and CRISP (the older, legacy format). Rows are deduplicated on applID and additionally rows with identical text are dropped (mostly administrative grants).

Light preprocessing is applied to remove extra spaces and [repeated header text](P3_analyze_headers.py). 

    ✔ Saved to data/NIH_ExPORTER_awarded_grant_text.jsonl.zst
    ℹ Saved 939,668 applications
    ℹ Uncompressed filesize 2,081,861,785
    ℹ Compressed filesize     630,780,318

Data souce temporary hosted at https://drive.google.com/file/d/1JBWxOIS0_EmmrMU6eJFtQtX6XAX9ULhw/view?usp=sharing