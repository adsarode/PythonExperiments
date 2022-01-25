import glob
import os

pattern = "C:/SOURCE_BASE/TA3D/TechArtisan3D/**/*.cpp"

numLines = 0
totalLines = 0
for item in glob.iglob(pattern, recursive=True):
    fileName = os.path.basename(item)
    with open(item) as f:
        numLines = sum(1 for line in f if line.strip())
    #print(fileName, numLines)
    totalLines += numLines

print("Total Number of Lines in Project = ", totalLines)
