S3_PUT_OBJECT_RESPONSE = {
    'ResponseMetadata':
    {
        'RequestId': 'x',
        'HostId': 'x',
        'HTTPStatusCode': 200,
        'HTTPHeaders':
        {
            'x-amz-id-2': 'x',
            'x-amz-request-id': 'x',
            'date': 'Sun, 16 Jan 2022 14:58:46 GMT',
            'etag': '"x"',
            'server': 'AmazonS3',
            'content-length': '0'
        },
        'RetryAttempts': 0
    },
    'ETag': '"x"'
}

S3_LIST_OBJECTS_RESPONSE_WITH_CONTENTS = {
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

S3_LIST_OBJECTS_RESPONSE_WITHOUT_CONTENTS = {
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
