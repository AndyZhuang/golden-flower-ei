import json
import subprocess

out = subprocess.check_output(
    ["gh", "release", "view", "v1.50.0", "--repo", "aaif-goose/goose", "--json", "assets"]
)
data = json.loads(out)
for a in data["assets"]:
    n = a["name"].lower()
    if "windows" in n or "msvc" in n or n.endswith(".exe") or n.endswith(".zip"):
        print(f"{a['name']}\t{a['size']:,} bytes\t{a.get('url','')}")
