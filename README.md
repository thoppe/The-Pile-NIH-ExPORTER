# The-Pile-NIH-ExPORTER

Download, parse, and filter NIH-awarded grant data from [ExPORTER](https://exporter.nih.gov/), data-ready for [The-Pile](https://github.com/EleutherAI/The-Pile).

Data is pulled from both RePORTER and CRISP (the older, legacy format). Rows are deduplicated on applID and additionally rows with identical text are dropped (mostly administrative grants).

Light preprocessing is applied to remove extra spaces and [repeated header text](P3_analyze_headers.py).

### Pile-V2 Statistics

    ✔ Saved to data/NIH_ExPORTER_awarded_grant_text.jsonl.zst
    ℹ Date collection completed: 12/14/2021
    ℹ 985,651 applications (45,983 added, 4.9% growth)
    ℹ Uncompressed filesize 2,198,670,684
    ℹ Compressed filesize     664,022,839
    ℹ sha256sum 0db76318737fda6c2a2484b809bb53e9e42952c284c0bf2b8862e8428e154833

### Pile-V1 Statistics

    ✔ Saved to data/NIH_ExPORTER_awarded_grant_text.jsonl.zst
    ℹ 939,668 applications
    ℹ Uncompressed filesize 2,081,861,427
    ℹ Compressed filesize     630,784,092
    ℹ sha256sum be7fc69b9a3652391b6567891b99277ac99e7dfd5892ba19cb312f909357c458