"""Keeps a copy of every shields.io badge in assets/badges/ and points README.md at the copies.

GitHub loads README images through its own image proxy, which gives up on shields.io after a few
seconds. On 2026-10-11 that left 7 to 9 of the 31 badges blank on any given page load, the star
and fork counts among them. Files in this repo are served by GitHub itself and always load.

badges.json maps each saved file to the shields.io URL it came from. A badge that fails to
download keeps yesterday's copy. Any new shields.io URL typed into the README is picked up and
swapped on the next run.
"""
import hashlib, json, os, re, time, urllib.request

DIR = "assets/badges"
MANIFEST = os.path.join(DIR, "badges.json")
RAW = "https://raw.githubusercontent.com/nicedreamzapp/nicedreamzapp/main/" + DIR + "/"

os.makedirs(DIR, exist_ok=True)
manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
by_url = {u: f for f, u in manifest.items()}


def name_for(url):
    path = url.split("img.shields.io/", 1)[1].split("?", 1)[0]
    m = re.search(r"badge-([a-z0-9-]+)\.json", url)
    if path == "endpoint" and m:
        path = "app-" + m.group(1)
    slug = re.sub(r"[^a-z0-9]+", "-", path.lower().replace("nicedreamzapp/", "")).strip("-")[:48]
    return "%s-%s.svg" % (slug, hashlib.md5(url.encode()).hexdigest()[:6])


def fetch(url):
    for wait in (0, 3, 10):
        time.sleep(wait)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "nicedreamzapp-profile-badges"})
            body = urllib.request.urlopen(req, timeout=30).read()
            if body.lstrip().startswith(b"<svg") and b"</svg>" in body:
                return body
        except Exception as e:
            print("retry", url[:80], e)
    return None


p = "README.md"
md = open(p).read()
for url in sorted(set(re.findall(r"https://img\.shields\.io/[^\s)\"']+", md))):
    if url not in by_url:
        by_url[url] = name_for(url)

failed = 0
for url, fname in sorted(by_url.items(), key=lambda kv: kv[1]):
    body = fetch(url)
    path = os.path.join(DIR, fname)
    if body:
        open(path, "wb").write(body)
    else:
        failed += 1
        print("FAILED, keeping old copy:", url)
    # only point the README at a copy that exists
    if os.path.exists(path):
        md = md.replace(url, RAW + fname)

open(p, "w").write(md)
json.dump({f: u for u, f in sorted(by_url.items(), key=lambda kv: kv[1])}, open(MANIFEST, "w"), indent=1)
print("%d badges, %d failed" % (len(by_url), failed))
