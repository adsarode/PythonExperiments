import glob
import os

import sys

import numpy
import vtk

import time

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

pattern = 'D:/ProjectData/*Spline*.vtk'
def main():
    ren = vtkRenderer()
    for item in glob.iglob(pattern, recursive=True):
        reader = vtk.vtkPolyDataReader()
        reader.SetFileName(item)
        reader.Update()

        polydata = reader.GetOutput()

        mapper = vtkPolyDataMapper()
        mapper.SetInputData(polydata)

        actor = vtkActor()
        actor.SetMapper(mapper)

        ren.AddActor(actor)
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('DDD')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
