# Find all subdirectories and run TestApp.exe on all of them - written as bat file
import glob
import os

dirPath = 'D:/ProjectData/Data/TestData/'
pattern = dirPath + '/**/'
batFile = open(dirPath + '/RunTest.bat', "w")
for item in glob.iglob(pattern, recursive=False):
    #dirPath, dirName = os.path.split(os.path.dirname(item))
    batFile.write("TestApp.exe" + " \"" + os.path.dirname(item) + "\"\n")
