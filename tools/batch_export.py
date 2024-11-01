import bpy
import os
import argparse
import json
from pathlib import Path

def export_scene_to_json(blend_file_path, export_path):
    """
    Exports a Blender scene to JSON format.
    
    Args:
        blend_file_path (str): Path to the .blend file.
        export_path (str): Directory where the JSON file will be saved.
    """
    # Open the blend file
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)

    # Gather scene data
    scene_data = {"objects": []}
    for obj in bpy.context.scene.objects:
        obj_data = {
            "name": obj.name,
            "type": obj.type,
            "location": list(obj.location),
            "rotation": list(obj.rotation_euler),
            "scale": list(obj.scale),
        }
        scene_data["objects"].append(obj_data)

    # Define output path and save JSON
    scene_name = Path(blend_file_path).stem
    json_path = os.path.join(export_path, f"{scene_name}.json")
    os.makedirs(export_path, exist_ok=True)
    with open(json_path, 'w') as json_file:
        json.dump(scene_data, json_file, indent=4)
    print(f"Exported scene to JSON: {json_path}")

def batch_export(directory, export_path, format="json"):
    """
    Batch exports all Blender files in a directory to a specified format.
    
    Args:
        directory (str): Directory containing .blend files.
        export_path (str): Directory where exported files will be saved.
        format (str): Export format ("json" or "fbx").
    """
    blend_files = [f for f in Path(directory).glob("**/*.blend")]

    if not blend_files:
        print("No .blend files found in the specified directory.")
        return

    for blend_file in blend_files:
        print(f"Processing file: {blend_file}")
        if format == "json":
            export_scene_to_json(str(blend_file), export_path)
        elif format == "fbx":
            export_scene_to_fbx(str(blend_file), export_path)
        else:
            print(f"Unsupported format: {format}. Only 'json' and 'fbx' are supported.")

def export_scene_to_fbx(blend_file_path, export_path):
    """
    Exports a Blender scene to FBX format.
    
    Args:
        blend_file_path (str): Path to the .blend file.
        export_path (str): Directory where the FBX file will be saved.
    """
    # Open the blend file
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)
    
    # Define output path
    scene_name = Path(blend_file_path).stem
    fbx_path = os.path.join(export_path, f"{scene_name}.fbx")
    os.makedirs(export_path, exist_ok=True)
    
    # Export scene to FBX
    bpy.ops.export_scene.fbx(filepath=fbx_path)
    print(f"Exported scene to FBX: {fbx_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch export Blender scenes to JSON or FBX.")
    parser.add_argument("directory", type=str, help="Directory containing .blend files.")
    parser.add_argument("export_path", type=str, help="Directory to save exported files.")
    parser.add_argument("--format", type=str, choices=["json", "fbx"], default="json", help="Export format (default: json).")

    args = parser.parse_args()

    # Run the batch export
    batch_export(args.directory, args.export_path, args.format)