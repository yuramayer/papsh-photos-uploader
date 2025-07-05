"""App keys for the python script"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_checked_env(env_name: str) -> str:
    """
    Environment checker for the config module

    Args:
        env_name (str): The environment variable name from .env file

    Returns:
        str: Checked environment variable string value
    """
    env = os.getenv(env_name)
    if not env:
        raise RuntimeError(f"The required variable isn't defined: {env_name}")
    return str(env)


CLOUD_S3_ID_KEY = get_checked_env('CLOUD_S3_ID_KEY')
CLOUD_S3_SECRET_KEY = get_checked_env('CLOUD_S3_SECRET_KEY')
BUCKET_NAME = get_checked_env('BUCKET_NAME')
