import glob
import os

#Rename file contents
def renameInsideFile(fname, subStrBefore, subStrAfter):
    with open(fname) as f:
        newText=f.read().replace(subStrBefore, subStrAfter)

    with open(fname, "w") as f:
        f.write(newText)

findStr = 'ABCProjXYZ'
pattern = 'C:/SOURCE_BASE/Projects/Test/**/*' + findStr + '*'
replaceStr = 'NewProjName'

#Rename directories
for exstPath in glob.iglob(pattern, recursive=True):
    if os.path.isdir(exstPath):
        existingName = os.path.basename(exstPath)
        newName = existingName.replace(findStr, replaceStr)
        newPath = os.path.dirname(exstPath) + '/'+ newName
        os.rename(exstPath, newPath)

#Rename files
for exstPath in glob.iglob(pattern, recursive=True):
    if not os.path.isdir(exstPath):
        existingName = os.path.basename(exstPath)
        newName = existingName.replace(findStr, replaceStr)
        newPath = os.path.dirname(exstPath) + '/'+ newName
        os.rename(exstPath, newPath)
        renameInsideFile(newPath, findStr, replaceStr)

