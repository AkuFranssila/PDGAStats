from utils.s3Utils.client import awsClient
from botocore.stub import Stubber


def mock_aws_client():
    stubber = Stubber(awsClient)
    stubber.activate()
