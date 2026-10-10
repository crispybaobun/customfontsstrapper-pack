"""Zip tidalfont/ into tidalfont.zip with pack.mcmeta at the zip's top level.

Usage: python build-pack.py [source_dir] [output_zip]
Defaults to tidalfont/ and tidalfont.zip next to this script.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

here = Path(__file__).resolve().parent
src = Path(sys.argv[1]) if len(sys.argv) > 1 else here / "tidalfont"
out = Path(sys.argv[2]) if len(sys.argv) > 2 else here / "tidalfont.zip"

if not (src / "pack.mcmeta").is_file():
    sys.exit(f"no pack.mcmeta in {src}")

files = sorted(p for p in src.rglob("*") if p.is_file())
for p in files:
    if p.suffix in (".json", ".mcmeta"):
        json.loads(p.read_text(encoding="utf-8"))

with zipfile.ZipFile(out, "w") as z:
    for p in files:
        # as_posix() gives forward slashes; the fixed date keeps the SHA-1
        # the same whenever the contents are the same.
        info = zipfile.ZipInfo(p.relative_to(src).as_posix(), (1980, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, p.read_bytes())

with zipfile.ZipFile(out) as z:
    names = z.namelist()
    if z.testzip() or "pack.mcmeta" not in names or any("\\" in n for n in names):
        sys.exit("bad zip: check entry names")
    for i in z.infolist():
        print(f"{i.file_size:>8}  {i.filename}")

print("zip: ", out)
print("sha1:", hashlib.sha1(out.read_bytes()).hexdigest())
