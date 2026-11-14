import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
# Verify the output is a complete, valid PNG matching the source.
with open(SRC, "rb") as f:
    src_head = f.read(8)
with open(DST, "rb") as f:
    dst_head = f.read(8)
assert src_head == dst_head == b"\x89PNG\r\n\x1a\n", "output is not a valid PNG"
assert os.path.getsize(DST) == os.path.getsize(SRC), "output size differs from source"
print(f"Wrote {DST} ({os.path.getsize(DST)} bytes)")
