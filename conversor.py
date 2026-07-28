import SimpleITK as sitk

print("1. Procurando fatias DICOM na pasta...")
# Acha todos os arquivos da série DICOM na pasta
reader = sitk.ImageSeriesReader()
dicom_names = reader.GetGDCMSeriesFileNames("C:/cranio_dicom/DICOM")
reader.SetFileNames(dicom_names)

print("2. Descompactando o volume 3D (Isso pode levar de 10 a 30 segundos)...")
image = reader.Execute()

print("3. Salvando como um volume unico (volume.mha)...")
sitk.WriteImage(image, "C:/cranio_dicom/volume.mha")

print("SUCESSO! O arquivo volume.mha foi criado na sua pasta.")