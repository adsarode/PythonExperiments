import glob
import os

# search files like abc.txt, abd.txt
 #'D:\ProjectData\BriusData\TestData\BracketTestScanned'
#path = 'C:\SOURCE_BASE\Brius\Data\BracketTestScanned\**\*Dumps'
#fileDump= glob.glob(path+'\**\*.stl*')
pattern = 'C:\SOURCE_BASE\Brius\Data\BracketTestScanned\**\*Dumps*\**\*.stl*'
for item in glob.iglob(pattern, recursive=True):
    print (item)
    #os.remove(item)
