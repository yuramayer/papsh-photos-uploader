"""Module with the additional funs"""

import os


def is_existing_directory(path: str) -> bool:
    """
    Check whether the given path exists and is a directory.

    Args:
        path (str): The filesystem path to check.

    Returns:
        bool: True if the path exists and is a directory, False otherwise.
    """
    return os.path.isdir(path)


def has_photos_files(path: str) -> bool:
    """
    Check whether the directory at the given path contains image files
    with .png or .jpg extension (case-insensitive).

    Args:
        path (str): The directory path to search in.

    Returns:
        bool: True if at least one .png or .jpg file exists, False otherwise.
    """
    for filename in os.listdir(path):
        if filename.lower().endswith(('.png', '.jpg')):
            return True

    return False
