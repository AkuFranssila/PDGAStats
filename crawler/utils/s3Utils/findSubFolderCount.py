import logging

from utils.s3Utils.client import awsClient


logging.getLogger().setLevel("INFO")


def find_sub_folder_count(folder_name: str, aws_client: any) -> str:
    """
    Get the next subfolder count from S3 bucket for selected folder. 

    If no folder with only digits in the name found, returns 0 as the start folder.
    """
    response = aws_client.list_objects_v2(
        Bucket="pdga-project-data",
        Prefix=f"{folder_name}/"
    )

    sub_folders = response.get('Contents', [])
    digit_sub_folders = []

    for s3_object in sub_folders:
        folder_name = s3_object.get("Key", None)
        if folder_name.isdigit():
            digit_sub_folders.append(folder_name)

    if digit_sub_folders:
        highest_folder_count = str(int(max(digit_sub_folders)) + 1)
    else:
        highest_folder_count = "0"

    return highest_folder_count
