"""food-picture-01 entry: copy the ramen picture to the grader's output dir.

The picture is entry.png beside this file. The grader runs this program in a
fresh container with the repository read-only at /bot and a writable /output;
outside the container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_DIR.mkdir(parents=True, exist_ok=True)

shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
