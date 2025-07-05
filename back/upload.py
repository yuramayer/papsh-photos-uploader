"""File uploader to the S3 bucket"""

from pathlib import Path
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from botocore.config import Config
from config import CLOUD_S3_ID_KEY, CLOUD_S3_SECRET_KEY, BUCKET_NAME


s3 = boto3.client(
    aws_access_key_id=CLOUD_S3_ID_KEY,
    aws_secret_access_key=CLOUD_S3_SECRET_KEY,
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net',
    region_name='ru-central1',
    config=Config(signature_version='s3v4')
)


def upload_photos_to_s3(directory: Path) -> list[str]:
    """
    Upload all photo files in the given directory to the S3 bucket

    Args:
        directory (Path): Directory with photo files

    Returns:
        list[str]: Filenames of photos that failed to upload
    """
    allowed_extensions = {'.png', '.jpg', '.jpeg'}
    failed_uploads = []

    for photo_path in directory.iterdir():
        if not photo_path.is_file():
            continue
        if photo_path.suffix.lower() not in allowed_extensions:
            continue

        key = photo_path.name
        try:
            s3.upload_file(str(photo_path), BUCKET_NAME, key)
        except (BotoCoreError, ClientError):
            failed_uploads.append(key)

    return failed_uploads
