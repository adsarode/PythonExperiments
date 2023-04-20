import os
import logging
from pathlib import Path
from shutil import unpack_archive

zip_files = Path(r"D:\ProjectData").rglob("*.zip")
while True:
    try:
        path = next(zip_files)
    except StopIteration:
        break # no more files
    except PermissionError:
        logging.exception("permission error")
    else:
        os.remove(path)
