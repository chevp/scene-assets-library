
# Scene Assets Library

The `scene-assets-library` is a structured directory that houses all assets related to scene creation and management for a large-scale project. 
This folder is designed to support scalability and ease of navigation, ensuring that assets like environment data, character files, props, and textures are well-organized 
and accessible for team members and automated processes.

## Folder Structure

The `scene-assets-library` is organized into subdirectories that help keep various types of assets separate, allowing for easy access, version control, and scalability.

### Root Structure

```plaintext
scene-assets-library/
├── environments/                  # Contains environments for various scene settings
│   ├── environment_name/
│   │   ├── scenes/                # Holds different scenes within the environment
│   │   │   ├── scene_name/
│   │   │   │   ├── version_1/
│   │   │   │   │   ├── scene.json          # JSON representation of the scene
│   │   │   │   │   ├── preview.png         # Thumbnail/preview image of the scene
│   │   │   │   │   └── metadata.json       # Metadata describing the scene version, authorship, and dependencies
│   │   │   │   └── ...
│   │   │   └── latest/                     # Symlink to the latest version
│   │   └── references/                     # Reference images or docs for the environment
│   └── ...
├── characters/                   # Library of character assets with textures, animations, and configurations
│   ├── character_name/
│   │   ├── version_1/
│   │   ├── latest/
│   └── ...
├── props/                        # Reusable props like furniture, items, or other scene objects
├── shaders/                      # Shaders and lighting configurations
├── textures/                     # Reusable textures, shared across scenes, characters, and props
└── references/                   # Project-wide reference materials (concept art, designs, etc.)
```

## Usage

This `scene-assets-library` folder is intended to work with scripts and tools that automate asset management, versioning, and scene export. 
Python scripts in this project use this structure to ensure consistency and efficiency in handling assets.

### Example Workflow

1. **Adding a New Scene Version**:
   - Place the `.blend` file for the new scene version under `blender_files/environments/[environment_name]/[version_x].blend`.
   - Use the script `scene_exporter.py` to export the `scene.json` file, specifying the blend file path, export path, and version.

2. **Updating the Latest Version**:
   - The `update_latest_symlink.py` script automatically updates the `latest` symlink to point to the most recent version of a scene for easy access.

3. **Batch Export**:
   - Use `batch_export.py` to export multiple `.blend` files to `scene.json` files in bulk. This script iterates over the `blender_files/` folder and generates JSONs for all scenes.

### Example Command-Line Usage

Run these scripts from the console to simplify asset management:

```bash
# Export a single scene to JSON format
python scene_exporter.py /path/to/blender_files/environment_name/version_1.blend /path/to/scene-assets-library/environments/environment_name/scenes/scene_name 1

# Batch export all scenes
python batch_export.py /path/to/blender_files /path/to/scene-assets-library/environments

# Update the latest version symlink
python update_latest_symlink.py /path/to/scene-assets-library/environments/environment_name/scenes/scene_name
```

## Contributing

If you are adding new asset types or environments, ensure they are consistent with the existing structure. 
Add relevant documentation for any new asset types in this README or additional `.md` files under `docs/`.

---

For further guidance, refer to the specific guidelines in the `docs/` directory for each asset type, such as scene setup, character pipeline, and prop handling.
