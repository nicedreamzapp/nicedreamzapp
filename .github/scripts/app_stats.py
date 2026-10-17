"""Rewrites the app numbers in README.md from https://nicedreamzwholesale.com/software/stats.json.

The Mac mini rebuilds stats.json twice a day from Apple's sales reports and Google Play's install
files. This keeps the profile honest without anyone remembering to update it (the table was
typed by hand until 2026-09-27 and went stale within a week).
Only text between the <!--X:START--> / <!--X:END--> markers is touched.
"""
import json, re, time, urllib.request

URL = "https://nicedreamzwholesale.com/software/stats.json"


def fetch():
    # The site's firewall now and then answers a runner IP with 403; a retry gets through.
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (app-stats; +https://github.com/nicedreamzapp)"})
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:
            if attempt == 3:
                raise
            print(f"fetch failed ({e}), retrying")
            time.sleep(30 * (attempt + 1))


s = fetch()
t = s["totals"]
fmt = "{:,}".format


def since(ym):
    y, m = ym.split("-")
    return ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][int(m) - 1] + " " + y


def stars(a):
    r, n = a.get("rating"), a.get("ratings")
    return "★ %.1f (%d)" % (r, n) if r and n else "–"


rows = ["| App | Live since | Downloads | App Store | Google Play | New on iPhone, last 7 days | App Store rating |",
        "|---|---|---:|---:|---:|---:|:---:|"]
for a in s["apps"]:
    ap, pl = a["apple"], a["play"]
    rows.append("| **%s** | %s | **%s** | %s | %s | %s | %s |" % (
        a["name"], since(a["since"]), fmt(a["total"]), fmt(ap["downloads"]), fmt(pl["installs"]),
        fmt(ap["last7"]), stars(ap)))
rows.append("| **Total** | | **%s** | **%s** | **%s** | **%s** | |" % (
    fmt(t["downloads"]), fmt(t["apple"]), fmt(t["play"]), fmt(t["last7"])))
diff = t["last7"] - t["prev7"]
weeks = " → ".join(fmt(w) for w in s["weeks"])
stats = "\n".join([
    "> _Updated automatically **%s** from Apple's sales reports and Google Play's install reports. "
    "Downloads are first-time App Store downloads (no updates or re-downloads) plus Google Play installs; "
    "Google runs about two weeks behind._" % s["updated_human"],
    "", "\n".join(rows), "",
    "**New iPhone downloads per week, last 8 weeks:** %s (%s%d vs the week before)." % (weeks, "+" if diff >= 0 else "", diff),
])
line = ("5 apps on the App Store and Google Play, **%s downloads** so far "
        "(%s App Store, %s Google Play), %s new on iPhone in the last week." % (
            fmt(t["downloads"]), fmt(t["apple"]), fmt(t["play"]), fmt(t["last7"])))

# claude-code-local's star and fork counts, straight from GitHub (typed by hand until 2026-10-12)
repo = json.load(urllib.request.urlopen("https://api.github.com/repos/nicedreamzapp/claude-code-local", timeout=60))
ccl = "%s+ stars, %s forks" % (fmt(repo["stargazers_count"] // 100 * 100), fmt(repo["forks_count"]))

p = "README.md"
md = open(p).read()
for key, body in (("APP-STATS", stats), ("APPS-LINE", line), ("CCL", ccl)):
    md, n = re.subn(r"(<!--%s:START-->).*?(<!--%s:END-->)" % (key, key),
                    lambda m: m.group(1) + ("\n" if key == "APP-STATS" else "") + body + ("\n" if key == "APP-STATS" else "") + m.group(2),
                    md, flags=re.S)
    assert n == 1, key
open(p, "w").write(md)
