# Unzip all zip files in sub-folders 
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
        #extract_dir = path.with_name(path.stem) # To use same directory name as zip
        extract_dir = path.parent.absolute()
        unpack_archive(str(path), str(extract_dir), 'zip')
        #print(extract_dir)
        #print(path.parent.absolute())
        print("Completed, ", extract_dir)
