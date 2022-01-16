import unittest
from utils.s3Utils.findSubFolderCount import find_sub_folder_count
from utils.s3Utils.client import awsClient
from botocore.stub import Stubber
from botocore.exceptions import StubAssertionError


class TestPlayerRawDataRunner(unittest.TestCase):

    def test_should_return_correct_sub_folder_count_if_no_content(self):
        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)
        
        test_response = {
            'ResponseMetadata': {
                'RequestId': 'H9PEHJEP0V48GXC1', 
                'HostId': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                'HTTPStatusCode': 200, 
                'HTTPHeaders': {
                    'x-amz-id-2': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                    'x-amz-request-id': 'H9PEHJEP0V48GXC1', 
                    'date': 'Mon, 10 Jan 2022 18:47:34 GMT', 
                    'x-amz-bucket-region': 'eu-north-1', 
                    'content-type': 'application/xml', 
                    'transfer-encoding': 'chunked', 
                    'server': 'AmazonS3'}, 'RetryAttempts': 0
                 }, 
            'IsTruncated': False, 
            'Name': 'pdga-project-data', 
            'Prefix': 'player_raw_data/',
            'MaxKeys': 1000, 
            'EncodingType': 'url', 
            'KeyCount': 0
            }
        
        stubber.add_response(
            'list_objects_v2',
            test_response,
            {'Bucket': 'pdga-project-data', 'Prefix': 'player_raw_data/'}
        )
        stubber.activate()
        
        sub_folder_count = find_sub_folder_count('player_raw_data', aws_client)
        
        self.assertEqual(sub_folder_count, '0')
        
    def test_should_return_correct_sub_folder_count_if_content(self):
        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)
        
        test_response = {
            'ResponseMetadata': {
                'RequestId': 'H9PEHJEP0V48GXC1', 
                'HostId': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                'HTTPStatusCode': 200, 
                'HTTPHeaders': {
                    'x-amz-id-2': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                    'x-amz-request-id': 'H9PEHJEP0V48GXC1', 
                    'date': 'Mon, 10 Jan 2022 18:47:34 GMT', 
                    'x-amz-bucket-region': 'eu-north-1', 
                    'content-type': 'application/xml', 
                    'transfer-encoding': 'chunked', 
                    'server': 'AmazonS3'}, 'RetryAttempts': 0
                 }, 
            'IsTruncated': False, 
            'Name': 'pdga-project-data', 
            'Prefix': 'player_raw_data/',
            'MaxKeys': 1000, 
            'EncodingType': 'url', 
            'KeyCount': 0,
            'Contents': [
                {
                    'Key': '0',
                    'LastModified': 'Mon, 10 Jan 2022 18:47:34 GMT',
                    'ETag': 'string',
                    'Size': 123,
                    'StorageClass': 'STANDARD',
                    'Owner': {
                        'DisplayName': 'string',
                        'ID': 'string'
                    }
                },
                {
                    'Key': '1',
                    'LastModified': 'Mon, 10 Jan 2022 18:47:34 GMT',
                    'ETag': 'string',
                    'Size': 123,
                    'StorageClass': 'STANDARD',
                    'Owner': {
                        'DisplayName': 'string',
                        'ID': 'string'
                    }
                },
            ],
            }
        
        stubber.add_response(
            'list_objects_v2',
            test_response,
            {'Bucket': 'pdga-project-data', 'Prefix': 'player_raw_data/'}
        )
        stubber.activate()
        
        sub_folder_count = find_sub_folder_count('player_raw_data', aws_client)
        
        self.assertEqual(sub_folder_count, '2')
        
    def test_should_return_correct_sub_folder_count_if_content_skips_numbers(self):
        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)
        
        test_response = {
            'ResponseMetadata': {
                'RequestId': 'H9PEHJEP0V48GXC1', 
                'HostId': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                'HTTPStatusCode': 200, 
                'HTTPHeaders': {
                    'x-amz-id-2': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                    'x-amz-request-id': 'H9PEHJEP0V48GXC1', 
                    'date': 'Mon, 10 Jan 2022 18:47:34 GMT', 
                    'x-amz-bucket-region': 'eu-north-1', 
                    'content-type': 'application/xml', 
                    'transfer-encoding': 'chunked', 
                    'server': 'AmazonS3'}, 'RetryAttempts': 0
                 }, 
            'IsTruncated': False, 
            'Name': 'pdga-project-data', 
            'Prefix': 'player_raw_data/',
            'MaxKeys': 1000, 
            'EncodingType': 'url', 
            'KeyCount': 0,
            'Contents': [
                {
                    'Key': '0',
                    'LastModified': 'Mon, 10 Jan 2022 18:47:34 GMT',
                    'ETag': 'string',
                    'Size': 123,
                    'StorageClass': 'STANDARD',
                    'Owner': {
                        'DisplayName': 'string',
                        'ID': 'string'
                    }
                },
                {
                    'Key': '5',
                    'LastModified': 'Mon, 10 Jan 2022 18:47:34 GMT',
                    'ETag': 'string',
                    'Size': 123,
                    'StorageClass': 'STANDARD',
                    'Owner': {
                        'DisplayName': 'string',
                        'ID': 'string'
                    }
                },
            ],
            }
        
        stubber.add_response(
            'list_objects_v2',
            test_response,
            {'Bucket': 'pdga-project-data', 'Prefix': 'player_raw_data/'}
        )
        stubber.activate()
        
        sub_folder_count = find_sub_folder_count('player_raw_data', aws_client)
        
        self.assertEqual(sub_folder_count, '6')
        
    def test_should_return_correct_sub_folder_count_if_content_has_non_digits(self):
        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)
        
        test_response = {
            'ResponseMetadata': {
                'RequestId': 'H9PEHJEP0V48GXC1', 
                'HostId': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                'HTTPStatusCode': 200, 
                'HTTPHeaders': {
                    'x-amz-id-2': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                    'x-amz-request-id': 'H9PEHJEP0V48GXC1', 
                    'date': 'Mon, 10 Jan 2022 18:47:34 GMT', 
                    'x-amz-bucket-region': 'eu-north-1', 
                    'content-type': 'application/xml', 
                    'transfer-encoding': 'chunked', 
                    'server': 'AmazonS3'}, 'RetryAttempts': 0
                 }, 
            'IsTruncated': False, 
            'Name': 'pdga-project-data', 
            'Prefix': 'player_raw_data/',
            'MaxKeys': 1000, 
            'EncodingType': 'url', 
            'KeyCount': 0,
            'Contents': [
                {
                    'Key': '0',
                    'LastModified': 'Mon, 10 Jan 2022 18:47:34 GMT',
                    'ETag': 'string',
                    'Size': 123,
                    'StorageClass': 'STANDARD',
                    'Owner': {
                        'DisplayName': 'string',
                        'ID': 'string'
                    }
                },
                {
                    'Key': 'TEST NAME',
                    'LastModified': 'Mon, 10 Jan 2022 18:47:34 GMT',
                    'ETag': 'string',
                    'Size': 123,
                    'StorageClass': 'STANDARD',
                    'Owner': {
                        'DisplayName': 'string',
                        'ID': 'string'
                    }
                },
            ],
            }
        
        stubber.add_response(
            'list_objects_v2',
            test_response,
            {'Bucket': 'pdga-project-data', 'Prefix': 'player_raw_data/'}
        )
        stubber.activate()
        
        sub_folder_count = find_sub_folder_count('player_raw_data', aws_client)
        
        self.assertEqual(sub_folder_count, '1')
        
    def test_should_call_pdga_bucket(self):
        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)
        
        test_response = {
            'ResponseMetadata': {
                'RequestId': 'H9PEHJEP0V48GXC1', 
                'HostId': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                'HTTPStatusCode': 200, 
                'HTTPHeaders': {
                    'x-amz-id-2': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                    'x-amz-request-id': 'H9PEHJEP0V48GXC1', 
                    'date': 'Mon, 10 Jan 2022 18:47:34 GMT', 
                    'x-amz-bucket-region': 'eu-north-1', 
                    'content-type': 'application/xml', 
                    'transfer-encoding': 'chunked', 
                    'server': 'AmazonS3'}, 'RetryAttempts': 0
                 }, 
            'IsTruncated': False, 
            'Name': 'pdga-project-data', 
            'Prefix': 'player_raw_data/',
            'MaxKeys': 1000, 
            'EncodingType': 'url', 
            'KeyCount': 0,
            }
        
        stubber.add_response(
            'list_objects_v2',
            test_response,
            {'Bucket': 'non_pdga_bucket', 'Prefix': 'player_raw_data/'}
        )
        stubber.activate()
        
        with self.assertRaises(StubAssertionError):
            find_sub_folder_count('player_raw_data', aws_client)
            
    def test_should_call_with_given_prefix(self):
        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)
        
        test_response = {
            'ResponseMetadata': {
                'RequestId': 'H9PEHJEP0V48GXC1', 
                'HostId': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                'HTTPStatusCode': 200, 
                'HTTPHeaders': {
                    'x-amz-id-2': 'D0og2Sq3WFt0dFiXoUPyqLFPAcjDSBfLZzeccc8jG2kGFa8KMviaPWHaUQjj5pQ0yBZf6p0JZcw=', 
                    'x-amz-request-id': 'H9PEHJEP0V48GXC1', 
                    'date': 'Mon, 10 Jan 2022 18:47:34 GMT', 
                    'x-amz-bucket-region': 'eu-north-1', 
                    'content-type': 'application/xml', 
                    'transfer-encoding': 'chunked', 
                    'server': 'AmazonS3'}, 'RetryAttempts': 0
                 }, 
            'IsTruncated': False, 
            'Name': 'pdga-project-data', 
            'Prefix': 'player_raw_data/',
            'MaxKeys': 1000, 
            'EncodingType': 'url', 
            'KeyCount': 0,
            }
        
        stubber.add_response(
            'list_objects_v2',
            test_response,
            {'Bucket': 'pdga-project-data', 'Prefix': 'THIS_WAS_NOT_THE_RIGHT_CALL/'}
        )
        stubber.activate()
        
        with self.assertRaises(StubAssertionError):
            find_sub_folder_count('player_raw_data', aws_client)

if __name__ == '__main__':
    unittest.main()