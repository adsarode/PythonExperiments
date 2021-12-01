import glob
import os

pattern = 'C:\SOURCE_BASE\Data\**\*Dumps*\**\*.stl*'
for item in glob.iglob(pattern, recursive=True):
    print (item)
    #os.remove(item)
