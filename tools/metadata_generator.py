import os
import json
import argparse
from datetime import datetime
from pathlib import Path

def generate_metadata(asset_name, asset_type, author, version="1.0.0", dependencies=None):
    """
    Generates metadata for an asset.
    
    Args:
        asset_name (str): Name of the asset.
        asset_type (str): Type of the asset (e.g., "texture", "3d_model").
        author (str): Name of the asset's author.
        version (str): Version of the asset (default is "1.0.0").
        dependencies (list): List of dependencies for the asset (default is None).
    
    Returns:
        dict: Metadata for the asset.
    """
    metadata = {
        "name": asset_name,
        "type": asset_type,
        "author": author,
        "version": version,
        "created_at": datetime.now().isoformat(),
        "dependencies": dependencies or [],
    }
    return metadata

def save_metadata(metadata, metadata_path):
    """
    Saves metadata to a JSON file.
    
    Args:
        metadata (dict): Metadata to save.
        metadata_path (str): Path to save the metadata JSON file.
    """
    os.makedirs(os.path.dirname(metadata_path), exist_ok=True)
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)
    print(f"Metadata saved at {metadata_path}")

def update_metadata_file(metadata_path, new_data):
    """
    Updates an existing metadata file with new data.
    
    Args:
        metadata_path (str): Path to the metadata file.
        new_data (dict): New data to update the metadata with.
    """
    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            existing_metadata = json.load(f)
    else:
        existing_metadata = {}

    existing_metadata.update(new_data)
    save_metadata(existing_metadata, metadata_path)

def generate_metadata_for_directory(directory, author, asset_type):
    """
    Generates metadata.json files for each asset in a specified directory.
    
    Args:
        directory (str): Directory containing assets.
        author (str): Name of the author to include in the metadata.
        asset_type (str): Type of the assets (e.g., "texture", "3d_model").
    """
    for root, dirs, files in os.walk(directory):
        for asset_file in files:
            # Skip metadata.json files to avoid overwriting existing metadata files
            if asset_file == "metadata.json":
                continue
            
            # Filter for asset files, assuming they are images or 3D files
            if asset_file.endswith((".png", ".jpg", ".fbx", ".obj", ".blend")):
                asset_name = Path(asset_file).stem
                metadata_path = os.path.join(root, "metadata.json")

                # Generate new metadata if file doesn't exist, or update if it does
                if not os.path.exists(metadata_path):
                    metadata = generate_metadata(
                        asset_name=asset_name,
                        asset_type=asset_type,
                        author=author,
                        version="1.0.0",
                        dependencies=[]
                    )
                    save_metadata(metadata, metadata_path)
                else:
                    update_metadata_file(metadata_path, {"last_updated": datetime.now().isoformat()})

def list_existing_metadata(directory):
    """
    Lists all metadata files in a directory for review.
    
    Args:
        directory (str): Directory to search for metadata files.
    """
    metadata_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "metadata.json":
                metadata_files.append(os.path.join(root, file))
    
    if metadata_files:
        print("Found metadata files:")
        for metadata_file in metadata_files:
            print(metadata_file)
    else:
        print("No metadata files found in the specified directory.")
        
def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate metadata files for assets.")
    parser.add_argument("directory", type=str, help="Directory containing assets.")
    parser.add_argument("author", type=str, help="Author of the assets.")
    parser.add_argument("asset_type", type=str, help="Type of the assets (e.g., 'texture', '3d_model').")
    parser.add_argument("--list", action="store_true", help="List all existing metadata files.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    if args.list:
        list_existing_metadata(args.directory)
    else:
        generate_metadata_for_directory(args.directory, args.author, args.asset_type)