# Copyright 2024 chevp. All rights reserved.

import os
from utils.file_utils import create_directory, list_files_in_directory, file_exists
from utils.json_utils import read_json, write_json, update_json, validate_json_schema, pretty_print_json

ASSET_MANIFEST_PATH = "asset_manifest.json"

def load_asset_manifest():
    """
    Loads the asset manifest from the default path.
    
    Returns:
        dict: Parsed JSON content of the asset manifest, or None if it doesn't exist.
    """
    return read_json(ASSET_MANIFEST_PATH)

def add_asset_to_manifest(asset_data):
    """
    Adds a new asset to the asset manifest.
    
    Args:
        asset_data (dict): Data about the asset to add to the manifest.
    """
    asset_manifest = load_asset_manifest() or {"assets": []}
    asset_manifest["assets"].append(asset_data)
    write_json(asset_manifest, ASSET_MANIFEST_PATH)
    print(f"Added new asset: {asset_data['name']}")

def update_asset_in_manifest(asset_name, updated_data):
    """
    Updates an existing asset in the manifest.
    
    Args:
        asset_name (str): The name of the asset to update.
        updated_data (dict): New data to update the asset with.
    """
    asset_manifest = load_asset_manifest() or {"assets": []}
    for asset in asset_manifest["assets"]:
        if asset["name"] == asset_name:
            asset.update(updated_data)
            write_json(asset_manifest, ASSET_MANIFEST_PATH)
            print(f"Updated asset: {asset_name}")
            return
    print(f"Asset {asset_name} not found in manifest.")

def check_asset_integrity(asset_directory):
    """
    Checks the integrity of assets in a directory by verifying their existence.
    
    Args:
        asset_directory (str): Directory where assets are stored.
    
    Returns:
        dict: Dictionary with asset paths as keys and a boolean indicating existence.
    """
    integrity_report = {}
    manifest = load_asset_manifest()
    if not manifest:
        print("No manifest found.")
        return integrity_report

    for asset in manifest["assets"]:
        asset_path = os.path.join(asset_directory, asset["path"])
        integrity_report[asset_path] = file_exists(asset_path)
        status = "exists" if integrity_report[asset_path] else "missing"
        print(f"Asset {asset['name']} ({asset_path}): {status}")

    return integrity_report

def validate_asset_schema(asset_data, schema):
    """
    Validates an asset's data against a given schema.
    
    Args:
        asset_data (dict): Asset data to validate.
        schema (dict): Schema to validate against.
    
    Returns:
        bool: True if the asset data matches the schema, False otherwise.
    """
    return validate_json_schema(asset_data, schema)

def list_all_assets():
    """
    Lists all assets in the manifest.
    
    Returns:
        list: List of asset names.
    """
    manifest = load_asset_manifest()
    if not manifest:
        print("No manifest found.")
        return []
    
    asset_names = [asset["name"] for asset in manifest["assets"]]
    print("Assets in manifest:", asset_names)
    return asset_names

def pretty_print_manifest():
    """
    Pretty-prints the entire asset manifest for easy readability.
    """
    manifest = load_asset_manifest()
    if manifest:
        pretty_print_json(manifest)
    else:
        print("No manifest found.")

def remove_asset_from_manifest(asset_name):
    """
    Removes an asset from the asset manifest.
    
    Args:
        asset_name (str): Name of the asset to remove.
    """
    manifest = load_asset_manifest()
    if manifest:
        updated_assets = [asset for asset in manifest["assets"] if asset["name"] != asset_name]
        manifest["assets"] = updated_assets
        write_json(manifest, ASSET_MANIFEST_PATH)
        print(f"Removed asset: {asset_name}")
    else:
        print("No manifest found to update.")

def find_asset_by_name(asset_name):
    """
    Finds and returns asset data by name.
    
    Args:
        asset_name (str): Name of the asset to search for.
    
    Returns:
        dict: Asset data if found, otherwise None.
    """
    manifest = load_asset_manifest()
    if manifest:
        for asset in manifest["assets"]:
            if asset["name"] == asset_name:
                print(f"Asset found: {asset}")
                return asset
    print(f"Asset {asset_name} not found.")
    return None