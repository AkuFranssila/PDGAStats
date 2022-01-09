import boto3
from typing import Literal
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

awsServiceType: str = Literal['s3']

def awsClient(awsService: awsServiceType, debug: bool = False) -> any:
    if debug:
        boto3.set_stream_logger('')

    client = boto3.client(
        awsService,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )

    return client
    