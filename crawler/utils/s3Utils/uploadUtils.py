import logging
import json
from utils.generalUtils.errorUtils import raise_error

from mapping.s3_folder_mapping import S3_FOLDER_MAPPING

logging.getLogger().setLevel("INFO")


def upload_object_s3(folder_name: str, sub_folder_name: str, file_prefix: str, file_suffix: str, data: any, aws_client: any, bucket: str = "pdga-project-data") -> None:
    """
    Upload single object to S3
    """

    if folder_name not in S3_FOLDER_MAPPING:
        raise_error('INCORRECT_S3_FOLDER_NAME')

    s3_key = f'{folder_name}/{sub_folder_name}/{file_prefix}{file_suffix}.json'

    resp = aws_client.put_object(
        Body=json.dumps(
            data,
            indent=4
        ),
        Bucket=bucket,
        Key=s3_key
    )
