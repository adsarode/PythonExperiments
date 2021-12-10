import numpy as np
import vtk

reader = vtk.vtkPolyDataReader()
reader.SetFileName('C:/SOURCE_BASE/CutPlane_9.vtk')
reader.Update()

points = np.array( reader.GetOutput().GetPoints().GetData() )
