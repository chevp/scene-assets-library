# Copyright 2024 chevp. All rights reserved.

import json
import os

def read_json(file_path):
    """
    Reads a JSON file and returns its contents as a dictionary.
    
    Args:
        file_path (str): Path to the JSON file.
    
    Returns:
        dict: Parsed JSON content as a dictionary, or None if there was an error.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file at {file_path}: {e}")
        return None

def write_json(data, file_path):
    """
    Writes a dictionary to a file as JSON.
    
    Args:
        data (dict): Data to write to the JSON file.
        file_path (str): Path where the JSON file will be saved.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully wrote JSON to {file_path}")
    except IOError as e:
        print(f"Error writing JSON to {file_path}: {e}")

def update_json(file_path, new_data):
    """
    Updates an existing JSON file with new data.
    
    Args:
        file_path (str): Path to the JSON file to update.
        new_data (dict): Data to update the JSON file with.
    """
    data = read_json(file_path) or {}
    data.update(new_data)
    write_json(data, file_path)

def validate_json_schema(data, schema):
    """
    Validates JSON data against a schema (using a basic dictionary structure).
    
    Args:
        data (dict): JSON data to validate.
        schema (dict): A dictionary representing the expected structure.
    
    Returns:
        bool: True if data matches the schema, False otherwise.
    """
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            print(f"Validation failed: '{key}' is missing or not of type {expected_type.__name__}")
            return False
    return True

def merge_json_files(file_path1, file_path2, output_path):
    """
    Merges two JSON files and writes the result to a new file.
    Conflicting keys will be overridden by values from the second file.
    
    Args:
        file_path1 (str): Path to the first JSON file.
        file_path2 (str): Path to the second JSON file.
        output_path (str): Path to save the merged JSON file.
    """
    data1 = read_json(file_path1) or {}
    data2 = read_json(file_path2) or {}
    merged_data = {**data1, **data2}  # Conflicting keys will take values from data2
    write_json(merged_data, output_path)

def pretty_print_json(data):
    """
    Prints JSON data in a readable format.
    
    Args:
        data (dict): JSON data to print.
    """
    print(json.dumps(data, indent=4))

def search_key_in_json(data, key):
    """
    Searches for a key in a nested JSON structure.
    
    Args:
        data (dict): JSON data to search within.
        key (str): Key to search for.
    
    Returns:
        list: List of values found for the specified key.
    """
    results = []
    
    def search(data, key):
        if isinstance(data, dict):
            for k, v in data.items():
                if k == key:
                    results.append(v)
                elif isinstance(v, (dict, list)):
                    search(v, key)
        elif isinstance(data, list):
            for item in data:
                search(item, key)
    
    search(data, key)
    return results