import bpy
import json
import os
import argparse
from pathlib import Path

def export_scene_to_json(blend_file, output_dir):
    """
    Exports a Blender scene to JSON format.
    
    Args:
        blend_file (str): Path to the .blend file.
        output_dir (str): Directory where the JSON file will be saved.
    """
    # Open the .blend file
    bpy.ops.wm.open_mainfile(filepath=blend_file)

    # Prepare data structure for JSON export
    scene_data = {"objects": []}
    
    for obj in bpy.context.scene.objects:
        # Capture object details
        obj_data = {
            "name": obj.name,
            "type": obj.type,
            "location": list(obj.location),
            "rotation": list(obj.rotation_euler),
            "scale": list(obj.scale),
        }
        scene_data["objects"].append(obj_data)

    # Define output path and filename
    scene_name = Path(blend_file).stem
    json_file_path = os.path.join(output_dir, f"{scene_name}.json")
    os.makedirs(output_dir, exist_ok=True)

    # Write scene data to JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(scene_data, json_file, indent=4)
    print(f"Scene exported to JSON: {json_file_path}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Export Blender scene to JSON.")
    parser.add_argument("blend_file", type=str, help="Path to the .blend file to export.")
    parser.add_argument("output_dir", type=str, help="Directory where the JSON file will be saved.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    export_scene_to_json(args.blend_file, args.output_dir)