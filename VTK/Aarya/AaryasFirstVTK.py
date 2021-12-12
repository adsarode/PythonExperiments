#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkElevationFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def main():
    colors = vtkNamedColors()
    renderer = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    sphere = vtkSphereSource()
    sphere.SetPhiResolution(100)
    sphere.SetThetaResolution(16)
    sphere.SetCenter(2,0,0)
    sphere.SetRadius(69)
    sphere.Update()
    sphereGeom = sphere.GetOutput()
    
    cone = vtkConeSource()
    cone.SetRadius(40)
    cone.SetHeight(100)
    cone.SetResolution(50)
    cone.Update()
    coneGeom = cone.GetOutput()
    
    print('Number of points in sphere = ', sphereGeom.GetNumberOfPoints())
    print('Number of triangles in sphere = ', sphereGeom.GetNumberOfCells())
    
    print('Number of points in cone = ', coneGeom.GetNumberOfPoints())
    print('Number of triangles in cone = ', coneGeom.GetNumberOfCells())
        
    mapperS = vtkDataSetMapper()
    mapperS.SetInputData(sphereGeom)
    actorS = vtkActor()
    actorS.SetMapper(mapperS)
    actorS.GetProperty().SetColor(1.0,0.0,0.0)
    actorS.GetProperty().SetOpacity(0.5)
    renderer.AddActor(actorS)

    mapperC = vtkDataSetMapper()
    mapperC.SetInputData(coneGeom)
    actorC = vtkActor()
    actorC.SetMapper(mapperC)
    actorC.GetProperty().SetOpacity(0.5)
    renderer.AddActor(actorC)

    renderer.SetBackground(colors.GetColor3d('SlateGray'))
    renWin.SetSize(640, 480)
    renWin.SetWindowName('Aarya\'s First VTK Program')

    renWin.Render()

    # Interact with the data.
    iren.Start()


if __name__ == '__main__':
    main()
