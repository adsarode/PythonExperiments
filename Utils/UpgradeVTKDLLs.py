import glob
import os
import shutil

release82Dir = "C:/SOURCE_BASE/Installer/ReleaseComponents/"
release910Dir = "C:/SOURCE_BASE/Installer/ReleaseComponents910/"
vtk910Dir = "C:/VS_2019_INSTALL/VTK910/Release/bin/"

vtk82DLLs = []
for dllPath in glob.iglob(release82Dir + "vtk*.dll"):
    dllName = os.path.basename(dllPath)
    vtk82DLLs.append(dllName)
    
#print(vtk82DLLs)

vtk910AllDLLPaths = []
for dllPath in glob.iglob(vtk910Dir + "vtk*.dll"):
    
    vtk910AllDLLPaths.append(dllPath)
    
#print(vtk910AllDLLPaths)

vtk910ReqDLLPaths = []
for vtk910DLL in vtk910AllDLLPaths:
    for vtk82DLLName in vtk82DLLs:
        vtk82DLLName = vtk82DLLName.replace("8.2.dll", "")
        if vtk82DLLName in vtk910DLL:
            vtk910ReqDLLPaths.append(vtk910DLL)
            
for vtk910DLL in vtk910ReqDLLPaths:
    #print(vtk910DLL)
    dllName = os.path.basename(vtk910DLL)
    release910 = release910Dir + dllName
    shutil.copyfile(vtk910DLL, release910)
    
#print(len(vtk910ReqDLLPaths))
#print(len(vtk910AllDLLPaths))

