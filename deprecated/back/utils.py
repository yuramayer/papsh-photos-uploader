"""Module with the additional funs"""

from pathlib import Path
from back.errors import get_err_msg_notstr_path


def get_user_path() -> Path:
    """
    Ask user to input a path and safely convert it to Path object

    Returns:
        Path: Validated Path object

    Raises:
        ValueError: If input is not a valid string path
    """
    raw_input = input('Input the path to the dir with photos: ')

    try:
        path = Path(raw_input).expanduser().resolve(strict=False)
    except TypeError:
        err_msg_notstr_path = get_err_msg_notstr_path()
        raise ValueError(err_msg_notstr_path) from TypeError

    return path


def is_existing_directory(path: Path) -> bool:
    """
    Check whether the given path exists and is a directory

    Args:
        path (Path): The filesystem path to check

    Returns:
        bool: True if the path exists and is a directory, False otherwise
    """
    return path.is_dir()


def has_photos_files(path: Path) -> bool:
    """
    Check whether the directory at the given path contains image files
    with .png or .jpg/.jpeg extension (case-insensitive)

    Args:
        path (Path): The directory path to search in

    Returns:
        bool: True if at least one .png or .jpg file exists, False otherwise
    """
    return any(
        file.suffix.lower() in {'.png', '.jpg', '.jpeg'}
        for file in path.iterdir()
        if file.is_file()
    )


def report_upload_results(failed_uploads: list[str]) -> None:
    """
    Report the result of S3 upload based on failures

    Args:
        failed_uploads (list[str]): List of filenames that failed to upload
    """
    if not failed_uploads:
        print('\n✅ Все фото успешно загружены!')
    else:
        print('\n❌ Ошибка загрузки следующих файлов:')
        for name in failed_uploads:
            print(f' - {name}')
