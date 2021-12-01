import shutil
import os
import glob

rootdir = 'D:\ProjectData\TestData\'
for path in glob.glob(f'{rootdir}/*/**/Dump*/', recursive=True):
    print(path)
    shutil.rmtree(path)
