#!/usr/bin/env python3
"""Download chosen Commons photos (960px) into img/, 520px thumbs into t/, credits into credits.json.
Picks = candidate indexes from cand/<key>.json (made by _tools/commons_cands.py). Run: python3 fetch_photos.py"""
import json, hashlib, subprocess, time, os
from PIL import Image

UA = "TripPagesBot/1.0 (personal travel page; info.msam)"
PICK = {
    "yu": [0, 13, 1, 3, 6, 11, 15],
    "bund": [9, 10, 4, 1, 6, 2],
    "waibaidu": [5, 0, 1, 4],
    "ljz": [3, 12, 2],
    "tower": [1, 2, 9, 7, 8, 6],
    "wukang": [0, 5, 7, 12, 15],
    "anfu": [0, 5, 11, 4],
    "museum": [],
    "xlb": [],
    "pvg": [],
}
if os.path.exists("pick_extra.json"):
    PICK.update(json.load(open("pick_extra.json")))

def thumb_url(title, w=960):
    name = title.replace("File:", "", 1).replace(" ", "_")
    h = hashlib.md5(name.encode()).hexdigest()
    url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[:2]}/{name}/{w}px-{name}"
    return url + (".jpg" if name.lower().endswith(".png") else "")

credits = json.load(open("credits.json")) if os.path.exists("credits.json") else {}
for key, idxs in PICK.items():
    if not idxs:
        continue
    cands = json.load(open(f"cand/{key}.json"))
    for n, i in enumerate(idxs, 1):
        fn = f"{key}-{n}.jpg"
        c = cands[i]
        credits[fn] = dict(author=c["author"], lic=c["lic"], page=c["desc"], title=c["title"])
        if os.path.exists(f"img/{fn}"):
            continue
        for k in range(5):
            subprocess.run(["curl", "-s", "-L", "-A", UA, "-o", f"img/{fn}", thumb_url(c["title"])])
            try:
                Image.open(f"img/{fn}").verify()
                break
            except Exception:
                time.sleep(3 * (k + 1))
        im = Image.open(f"img/{fn}").convert("RGB")
        im.thumbnail((520, 520))
        im.save(f"t/{fn}", quality=78)
        print("ok", fn, c["title"][:60])
        time.sleep(2.5)
json.dump(credits, open("credits.json", "w"), ensure_ascii=False, indent=1)
print("credits", len(credits))
