"""Module with the messages for the errors"""


def get_err_msg_notstr_path() -> str:
    """Creates error message when path isn't str"""
    return (
        'The input string must be '
        'a string-like value'
    )


def get_err_msg_valid_path() -> str:
    """Creates error message when path doesn't exist"""
    return (
        'The input string should be valid '
        'path to the directory with photos'
    )


def get_err_msg_contains_photos() -> str:
    """Creates error message when there's no photos in dir"""
    return (
        'The directory should contain '
        'photos .jpg or .png'
    )
