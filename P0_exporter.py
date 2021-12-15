from pathlib import Path
import time
from wasabi import msg
import bs4
import requests
from dspipe import Pipe

url_exporter = "https://exporter.nih.gov/ExPORTER_Catalog.aspx?sid=0&index=1"
sess = requests.session()

base_url = "https://exporter.nih.gov/"

# Get the links from the target webpage
r = sess.get(url_exporter)

assert r.ok
soup = bs4.BeautifulSoup(r.content, "lxml")

# Filter for only our matches
target = "CSVs/final/RePORTER_"
save_links = [a["href"] for a in soup.find_all("a", href=True)]
save_links = [link for link in save_links if target in link]

msg.good(f"Found {len(save_links)} links in Exporter")


def download(f0, f1):
    url = base_url + f0

    r = sess.get(url)
    if not r.ok:
        print(r.content)
        print(r.status_code)
        msg.fail(f"Failed {url}")
        exit()

    with open(f1, "wb") as FOUT:
        FOUT.write(r.content)

    msg.good(f"Saved {f0}")
    time.sleep(5)


P = Pipe(save_links, "data/CSV", input_suffix=".zip", output_suffix=".zip")
P(download, 2)
