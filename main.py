import vtk

print("Iniciando renderizacao da mandibula...")

# ==========================================
# DADOS
# ==========================================
reader = vtk.vtkMetaImageReader()
reader.SetFileName("C:/cranio_dicom/volume.mha")
reader.Update()
print(f"-> Escala real de densidade do volume: {reader.GetOutput().GetScalarRange()}")

# ==========================================
# MAPEIA
# ==========================================
volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
volumeMapper.SetInputConnection(reader.GetOutputPort())

# Força alta resolução
volumeMapper.SetAutoAdjustSampleDistances(0) 
volumeMapper.SetSampleDistance(0.5) 

# --------------TESTE PADRAO ----------------------

opacityTransferFunction = vtk.vtkPiecewiseFunction()
opacityTransferFunction.AddPoint(-1000, 0.0) # Ar invisível
opacityTransferFunction.AddPoint(150,   0.0) # Pele e carne invisíveis
opacityTransferFunction.AddPoint(400,   0.9) # Osso bem sólido
opacityTransferFunction.AddPoint(3000,  1.0) # Dentes e ossos densos

colorTransferFunction = vtk.vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(150,  0.0, 0.0, 0.0)
colorTransferFunction.AddRGBPoint(400,  1.0, 0.98, 0.9) # Cor de osso/marfim
colorTransferFunction.AddRGBPoint(3000, 1.0, 1.0, 1.0)  # Branco puro

# -------------------------------------------------


# --------------TESTE 2 ROSTO ---------------------------
"""
opacityTransferFunction = vtk.vtkPiecewiseFunction()
opacityTransferFunction.AddPoint(-1000, 0.0)
opacityTransferFunction.AddPoint(-100,  0.0) # Remove o ar da sala
opacityTransferFunction.AddPoint(50,    0.8) # Pele sólida
opacityTransferFunction.AddPoint(150,   0.8) # Músculos
opacityTransferFunction.AddPoint(300,   0.0) # A partir daqui (osso), fica invisível

colorTransferFunction = vtk.vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(-100, 0.0, 0.0, 0.0)
colorTransferFunction.AddRGBPoint(50,   0.9, 0.6, 0.5) # Tom de pele
colorTransferFunction.AddRGBPoint(150,  0.8, 0.3, 0.3) # Tom avermelhado interno
"""
# -----------------------------------------------------

# ------------------TESTE 3 TRANSLUCIDO -------------------
"""
opacityTransferFunction = vtk.vtkPiecewiseFunction()
opacityTransferFunction.AddPoint(-1000, 0.0)
opacityTransferFunction.AddPoint(-100,  0.0)
opacityTransferFunction.AddPoint(50,    0.15) # Pele semi-transparente (15% de opacidade)
opacityTransferFunction.AddPoint(150,   0.2)
opacityTransferFunction.AddPoint(400,   0.95) # Osso sólido no fundo

colorTransferFunction = vtk.vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(-100, 0.0, 0.0, 0.0)
colorTransferFunction.AddRGBPoint(50,   0.8, 0.4, 0.3) # Pele avermelhada
colorTransferFunction.AddRGBPoint(400,  1.0, 0.95, 0.85) # Osso claro
"""
# --------------------------------------------------------------------

volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetColor(colorTransferFunction)
volumeProperty.SetScalarOpacity(opacityTransferFunction)
volumeProperty.ShadeOn()
volumeProperty.SetInterpolationTypeToLinear()

volumeProperty.SetAmbient(0.3)
volumeProperty.SetDiffuse(0.8)
volumeProperty.SetSpecular(0.2)
volumeProperty.SetSpecularPower(10.0)

volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

# ==========================================
# RENDERIZA
# ==========================================
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(800, 600)
renderWindow.SetWindowName("Trabalho 2 - Maloclusão Classe 3 MediModel")
renderWindow.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)

renderer.AddViewProp(volume)
renderer.SetBackground(1.0, 1.0, 1.0) # Fundo Branco

print("Abrindo Janela 3D. girar com o mouse.")
renderWindow.Render()
renderer.ResetCamera()
interactor.Start()