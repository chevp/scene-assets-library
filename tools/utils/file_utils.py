# Copyright 2024 chevp. All rights reserved.

import os
import json

def read_json(file_path):
    """
    Reads a JSON file and returns its contents.
    
    Args:
        file_path (str): Path to the JSON file.
    
    Returns:
        dict: Parsed JSON content as a dictionary.
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
    Writes a dictionary as JSON to a file.
    
    Args:
        data (dict): Data to write to the file.
        file_path (str): Path where JSON file will be saved.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully wrote JSON to {file_path}")
    except IOError as e:
        print(f"Error writing JSON to {file_path}: {e}")

def create_directory(path):
    """
    Creates a directory if it doesn't exist.
    
    Args:
        path (str): Directory path to create.
    """
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory created or already exists at {path}")
    except Exception as e:
        print(f"Error creating directory at {path}: {e}")

def list_files_in_directory(directory, extension=None):
    """
    Lists all files in a directory, optionally filtered by file extension.
    
    Args:
        directory (str): Path to the directory.
        extension (str, optional): File extension to filter by (e.g., '.json').
    
    Returns:
        list: List of file paths in the directory with the specified extension.
    """
    try:
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if not extension or filename.endswith(extension):
                    files.append(os.path.join(root, filename))
        return files
    except Exception as e:
        print(f"Error listing files in {directory}: {e}")
        return []

def file_exists(file_path):
    """
    Checks if a file exists at the given path.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def get_file_extension(file_path):
    """
    Gets the file extension from a file path.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: The file extension (e.g., '.json').
    """
    return os.path.splitext(file_path)[1]

def get_filename_without_extension(file_path):
    """
    Gets the file name without the extension from a file path.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: The file name without its extension.
    """
    return os.path.splitext(os.path.basename(file_path))[0]

def copy_file(src, dest):
    """
    Copies a file from source to destination.
    
    Args:
        src (str): Source file path.
        dest (str): Destination file path.
    """
    try:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy(src, dest)
        print(f"File copied from {src} to {dest}")
    except IOError as e:
        print(f"Error copying file from {src} to {dest}: {e}")

def delete_file(file_path):
    """
    Deletes a file at the given path.
    
    Args:
        file_path (str): Path to the file.
    """
    try:
        if file_exists(file_path):
            os.remove(file_path)
            print(f"File deleted at {file_path}")
    except Exception as e:
        print(f"Error deleting file at {file_path}: {e}")