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

renderer = vtkRenderer()
def CreatePlanet(radius, center):
    sphere = vtkSphereSource()
    sphere.SetPhiResolution(40)
    sphere.SetThetaResolution(40)
    sphere.SetCenter(center)
    sphere.SetRadius(radius)
    sphere.Update()
    sphereGeom = sphere.GetOutput()
    return sphereGeom

def CreateVisualization(geom):
    mapper = vtkDataSetMapper()
    mapper.SetInputData(geom)
    actor = vtkActor()
    actor.SetMapper(mapper)
    renderer.AddActor(actor)
    return actor

def main():
    colors = vtkNamedColors()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(renderer)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    earthCenter = [100.0,0.0,0.0]
    earth = CreatePlanet(4.0, earthCenter)
    
    marsCenter = [80.0,0.0,0.0]
    mars = CreatePlanet(3.0, marsCenter)

    sunCenter = [0.0,0.0,0.0]
    sun = CreatePlanet(15.0, sunCenter)
    
    earthActor = CreateVisualization(earth)
    earthActor.GetProperty().SetColor(colors.GetColor3d('Blue'))

    marsActor = CreateVisualization(mars)
    marsActor.GetProperty().SetColor(colors.GetColor3d('Red'))

    sunActor = CreateVisualization(sun)
    sunActor.GetProperty().SetColor(colors.GetColor3d('Yellow'))

    renderer.SetBackground(colors.GetColor3d('Black'))
    renWin.SetSize(640, 480)
    renWin.SetWindowName('Aarya\'s Solar System')

    renWin.Render()

    # Interact with the data.
    iren.Start()


if __name__ == '__main__':
    main()
