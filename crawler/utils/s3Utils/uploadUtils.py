import logging
import json

from utils.s3Utils.client import awsClient


logging.getLogger().setLevel("INFO")

client = awsClient("s3")

def uploadObjectS3(folderName: str, subFolderName: str, filePrefix: str, fileSuffix: str, data: any, bucket: str ="pdga-project-data") -> None:
    """
    Upload single object to S3
    """

    s3Key = f'{folderName}/{subFolderName}/{filePrefix}{fileSuffix}.json'
    
    client.put_object(Body=json.dumps(data, indent=4), Bucket=bucket, Key=s3Key)