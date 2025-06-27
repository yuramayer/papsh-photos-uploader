"""Main app module"""

from back.utils import is_existing_directory, has_photos_files
from back.errors import get_err_msg_valid_path, get_err_msg_contains_photos


def main():
    """Main app function"""

    path = input('Input the path to the dir with photos: ')

    if not is_existing_directory(path):
        err_msg_valid_path = get_err_msg_valid_path()
        raise ValueError(err_msg_valid_path)

    if not has_photos_files(path):
        err_msg_contains_photos = get_err_msg_contains_photos()
        raise ValueError(err_msg_contains_photos)
