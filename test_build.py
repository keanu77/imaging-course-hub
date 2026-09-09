"""Check standalone output, source coverage and public link isolation."""
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
class Inventory(HTMLParser):
    def __init__(self):
        super().__init__()
        self.classes = []
        self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.classes.extend(attrs.get("class", "").split())
        if "href" in attrs:
            self.links.append(attrs["href"])

rows = json.loads((ROOT / "video-sources.json").read_text())["records"]
core = [r for r in rows if r["learning_tier"] == "core"]
profiles = json.loads((ROOT / "channel-profiles.json").read_text())["channels"]
assert {p["channel"] for p in profiles} == {r["verified_channel"] for r in core}
for p in profiles:
    assert all(p[k].strip() for k in ("name_zh", "background_zh", "importance_zh", "when_zh", "reference_url"))
    assert p["reference_url"].startswith("https://")
for name in ("index.html", "sources.html"):
    html = (ROOT / "dist" / name).read_text()
    assert "{{" not in html and "127.0.0.1" not in html
    parser = Inventory()
    parser.feed(html)
    for link in parser.links:
        if link.startswith(("https://", "#")):
            continue
        assert (ROOT / "dist" / link.split("?")[0].split("#")[0]).exists(), link
    if name == "sources.html":
        assert parser.classes.count("provider-importance") == len(profiles)
        assert parser.classes.count("video-record") == len(rows)
assert not list((ROOT / "dist").glob("*-video-sources.csv"))
print("PASS standalone public build and channel explanations")
