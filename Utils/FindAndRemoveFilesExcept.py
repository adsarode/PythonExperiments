import glob
import os

pattern = 'C:\SOURCE_BASE\Data\**\*.json*'
keepSubstr = "Input"
for item in glob.iglob(pattern, recursive=True):
    fileName = os.path.basename(item)
    if fileName.find(keepSubstr) == -1:
        print(fileName)
        os.remove(item)
