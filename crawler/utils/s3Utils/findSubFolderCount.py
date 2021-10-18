import logging

from utils.s3Utils.client import awsClient


logging.getLogger().setLevel("INFO")
client = awsClient("s3")

def findSubFolderCount(folderName: str) -> str:
    """
    Get the next subfolder count from S3 bucket for selected folder. 

    If no folder with only digits in the name found, returns 0 as the start folder.
    """

    response = client.list_objects_v2(
        Bucket="pdga-project-data",
        Prefix=f"{folderName}/"
    )

    subFolders = response.get('Contents', [])
    digitSubFolders = []

    for s3Object in subFolders:
        folderName = s3Object.get("Key", None)
        if folderName.isdigit():
            digitSubFolders.append(folderName)

    if digitSubFolders:
        highestFolderCount = str(int(max(digitSubFolders)) + 1)
    else:
        highestFolderCount = "0"

    return highestFolderCount


