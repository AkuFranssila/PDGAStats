import unittest
import requests_mock
from botocore.stub import Stubber, ANY
from test.data.test_data_latest_id_160_000 import TEST_DATA_LATEST_ID_160_000

from runners.runPlayerRawData import run_player_raw_data, handle_arguments
from utils.s3Utils.client import awsClient
from utils.testUtils.requestsTestUtils import mock_requests_get
from utils.testUtils.aws_test_utils import S3_LIST_OBJECTS_RESPONSE_WITHOUT_CONTENTS, S3_PUT_OBJECT_RESPONSE, S3_LIST_OBJECTS_RESPONSE_WITH_CONTENTS
from test.data.test_data_pdga_44708 import test_data_pdga_44708
from test.data.test_data_latest_id_202725 import TEST_DATA_LATEST_ID_202725


class TestPlayerRawDataRunner(unittest.TestCase):

    def test_should_fail_if_no_arguments(self):
        with self.assertRaises(TypeError):
            handle_arguments([])

    @requests_mock.Mocker()
    def test_should_run_correctly_on_test(self, m):
        test_data = test_data_pdga_44708
        player_id_url = "https://www.pdga.com/player/1"
        mock_requests_get(player_id_url, test_data, m)

        player_id_url = "https://www.pdga.com/player/2"
        mock_requests_get(player_id_url, test_data, m)

        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)
        stubber.add_response(
            'put_object',
            S3_PUT_OBJECT_RESPONSE,
            {'Bucket': 'pdga-project-data',
                'Key': 'player_raw_data/test/1.json', 'Body': ANY}
        )

        # Third argument tests if requests matches the expected
        stubber.add_response(
            'put_object',
            S3_PUT_OBJECT_RESPONSE,
            {'Bucket': 'pdga-project-data',
                'Key': 'player_raw_data/test/2.json', 'Body': ANY}
        )
        stubber.activate()

        run_player_raw_data("test", 1, 2, aws_client)

    @requests_mock.Mocker()
    def test_should_run_correctly_on_custom(self, m):
        test_url = "https://www.pdga.com/players?FirstName=&LastName=&PDGANum=&Status=All&Class=All&MemberType=All&City=&StateProv=All&Country=All&Country_1=All&UpdateDate=&order=PDGANum&sort=desc"
        test_json = TEST_DATA_LATEST_ID_202725
        mock_requests_get(test_url, test_json, m)

        test_data = test_data_pdga_44708
        player_id_url = "https://www.pdga.com/player/202724"
        mock_requests_get(player_id_url, test_data, m)

        player_id_url = "https://www.pdga.com/player/202725"
        mock_requests_get(player_id_url, test_data, m)

        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)
        stubber.add_response(
            'list_objects_v2',
            S3_LIST_OBJECTS_RESPONSE_WITH_CONTENTS,
            {'Bucket': 'pdga-project-data', 'Prefix': 'player_raw_data/'}
        )

        stubber.add_response(
            'put_object',
            S3_PUT_OBJECT_RESPONSE,
            {'Bucket': 'pdga-project-data',
                'Key': 'player_raw_data/2/202724.json', 'Body': ANY}
        )

        # Third argument tests if requests matches the expected
        stubber.add_response(
            'put_object',
            S3_PUT_OBJECT_RESPONSE,
            {'Bucket': 'pdga-project-data',
                'Key': 'player_raw_data/2/202725.json', 'Body': ANY}
        )
        stubber.activate()

        run_player_raw_data("custom", 202724, 202725, aws_client)

    @requests_mock.Mocker()
    def test_should_run_correctly_on_all(self, m):
        test_url = "https://www.pdga.com/players?FirstName=&LastName=&PDGANum=&Status=All&Class=All&MemberType=All&City=&StateProv=All&Country=All&Country_1=All&UpdateDate=&order=PDGANum&sort=desc"
        test_json = TEST_DATA_LATEST_ID_160_000
        mock_requests_get(test_url, test_json, m)

        test_data = test_data_pdga_44708

        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)

        stubber.add_response(
            'list_objects_v2',
            S3_LIST_OBJECTS_RESPONSE_WITHOUT_CONTENTS,
            {'Bucket': 'pdga-project-data', 'Prefix': 'player_raw_data/'}
        )

        for i in range(159_950, 160_001):
            player_id_url = f"https://www.pdga.com/player/{str(i)}"
            mock_requests_get(player_id_url, test_data, m)
            stubber.add_response(
                'put_object',
                S3_PUT_OBJECT_RESPONSE,
                {
                    'Bucket': 'pdga-project-data',
                    'Key': f'player_raw_data/0/{str(i)}.json', 'Body': ANY
                }
            )
        stubber.activate()

        run_player_raw_data("all", 159_950, 422322, aws_client)


if __name__ == '__main__':
    unittest.main()
