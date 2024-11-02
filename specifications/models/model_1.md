# GLTF Model Specification for Blender

This document outlines the specifications for creating a GLTF model in Blender, focusing on its appearance, animations, and size.

## Model Overview

- **Name**: EntityName
- **Description**: Brief description of the model's purpose and functionality.
- **Creator**: Your Name / Your Team Name
- **Creation Date**: YYYY-MM-DD

## Appearance

### Dimensions

- **Scale**: Ensure the model is scaled appropriately in Blender. The default scale for GLTF models is usually 1 unit = 1 meter.
- **Size**:
  - **Width**: X meters
  - **Height**: Y meters
  - **Depth**: Z meters

### Materials

- **Base Color**: Specify the base color or texture used.
- **Textures**:
  - **Diffuse Texture**: File path and description.
  - **Normal Map**: File path and description.
  - **Metallic Map**: File path and description.
  - **Roughness Map**: File path and description.

## Animations

### Animation Overview

- **Total Animations**: Number of animations included with the model.
- **Animation Length**: Specify the duration of each animation.

### Animation List

1. **Animation Name**: Walk
   - **Duration**: 2 seconds
   - **Frame Range**: 1 - 48
   - **Description**: Description of the walk animation.

2. **Animation Name**: Run
   - **Duration**: 1.5 seconds
   - **Frame Range**: 49 - 96
   - **Description**: Description of the run animation.

3. **Animation Name**: Idle
   - **Duration**: 3 seconds
   - **Frame Range**: 97 - 144
   - **Description**: Description of the idle animation.

### Animation Export Settings

- **Export Format**: GLTF (.gltf or .glb)
- **Keyframe Settings**: Describe keyframe interpolation settings (e.g., linear, bezier).
- **Animation Compression**: Specify whether animation compression is used and its settings.

## Export Settings

- **File Format**: GLTF (glTF 2.0)
- **Export Path**: Specify where the model will be exported.
- **Settings**:
  - **Include Normals**: Yes
  - **Include UVs**: Yes
  - **Include Materials**: Yes
  - **Animation Export**: Yes

## References

- [GLTF Specification](https://www.khronos.org/gltf/)
- [Blender Documentation](https://docs.blender.org/manual/en/latest/)