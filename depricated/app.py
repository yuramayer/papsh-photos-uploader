"""Papsh photos uploader to the S3"""

from back.utils import (
    is_existing_directory,
    has_photos_files,
    get_user_path,
    report_upload_results
)
from back.upload import (
    upload_photos_to_s3
)
from back.errors import (
    get_err_msg_valid_path,
    get_err_msg_contains_photos
)


def main():
    """Takes the path from the user & sends the photos to the S3 Cloud"""

    path = get_user_path()

    if not is_existing_directory(path):
        err_msg_valid_path = get_err_msg_valid_path()
        raise ValueError(err_msg_valid_path)

    if not has_photos_files(path):
        err_msg_contains_photos = get_err_msg_contains_photos()
        raise ValueError(err_msg_contains_photos)

    failed_uploads = upload_photos_to_s3(path)
    report_upload_results(failed_uploads)
