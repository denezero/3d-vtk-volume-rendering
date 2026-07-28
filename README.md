[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![VTK](https://img.shields.io/badge/VTK-9.0+-green.svg)](https://vtk.org/download/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
# 3D Volumetric Medical Image Visualization
## Overview

**3D Volumetric Medical Image Visualization** is a powerful Python-based pipeline for processing and rendering medical imaging data (Computed Tomography). By leveraging GPU-accelerated **Volume Rendering** via *Ray Casting*, it transforms raw 2D DICOM series into a fully interactive 3D environment, allowing for dynamic segmentation and exploration of anatomical structures.

## Features

- **Reliable Data Unification**: Seamlessly process and decompress raw DICOM slices (including *JPEG Lossless* scans) into a clean, single `.mha` volumetric file using SimpleITK.
- **High-Performance Rendering**: Offloads heavy spatial calculations and ray-casting directly to the GPU via `vtkGPUVolumeRayCastMapper`.
- **Dynamic Tissue Segmentation**: Isolate specific anatomical structures instantly using transfer functions based on the Hounsfield (HU) scale.
- **Zero-Reload Interactivity**: Switch between visualization modes on-the-fly using keyboard observers—no memory reloading or application restarts required.
- **Trackball Camera**: Smooth, native 3D interaction for rotating, zooming, and panning around the medical model.

## Installation

### Prerequisites
- Python 3.8 or higher
- A dedicated or modern integrated GPU to handle VTK Ray Casting

### Setup
Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone [https://github.com/your-username/3d-medical-visualization.git](https://github.com/your-username/3d-medical-visualization.git)
cd 3d-medical-visualization

# Install the required libraries
pip install vtk SimpleITK

```

## Usage

The application flow is divided into data preparation and visual inspection.

### 1. Data Preprocessing

Before rendering, compile your individual DICOM slices into a continuous 3D volume. Edit `conversor.py` to point to your local DICOM directory, then run:

Bash

```
python conversor.py
```

_This will output a `volume.mha` file in your specified directory._

### 2. 3D Visualization

Once the `.mha` volume is generated, launch the interactive viewer:

Bash

```
python main.py
```

### Controls & View Modes
Interact with the 3D scene using your mouse (Left-click to rotate, Scroll to zoom). Use the keyboard numbers to switch between specialized medical filters:

- **[ 1 ] Bone Mode**: Filters out air and soft tissues, rendering only the skeletal structure with maximum opacity.
  
  ![Bone Mode Preview](gif/Bone_Mode_Preview.gif)

- **[ 2 ] Soft Tissue Mode**: Hides the internal skeletal structure, highlighting the patient's epidermis and facial muscles.
  
  ![Bone Mode Preview](gif/Soft_Tissue_Preview.gif)

- **[ 3 ] X-Ray (Translucent) Mode**: Overlays views by assigning 15% opacity to the skin, revealing the solid bones inside.
  
  ![Bone Mode Preview](gif/X-Ray_Mode_Preview.gif)

    

## Contributing & Maintenance

This project is actively maintained for educational purposes in computer graphics, biometrics, and healthcare technology. We welcome contributions from software engineers and medical professionals!

If you'd like to improve the shading algorithms (`ShadeOn`), optimize performance, or add UI elements, please read our [Contribution Guidelines](CONTRIBUTING) before submitting a Pull Request.

## License

This project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
