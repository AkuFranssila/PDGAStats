import unittest
import requests_mock
from botocore.stub import Stubber, ANY
from utils.s3Utils.client import awsClient
from utils.testUtils.requestsTestUtils import mock_requests_get
from utils.testUtils.aws_test_utils import S3_LIST_OBJECTS_RESPONSE_WITHOUT_CONTENTS, S3_PUT_OBJECT_RESPONSE, S3_LIST_OBJECTS_RESPONSE_WITH_CONTENTS

from runners.run_tournament_raw_data import handle_arguments, run_tournament_raw_data

from test.data.test_data_tournament_49356 import TEST_DATA_TOURNAMENT_49356
from test.data.test_data_tournament_50816 import TEST_DATA_TOURNAMENT_50816
from test.data.test_data_tournament_last_page_test import TEST_DATA_TOURNAMENT_LAST_PAGE_TEST

TOURNAMENT_URL_49356 = "https://www.pdga.com/tour/event/49356"
TOURNAMENT_URL_50816 = "https://www.pdga.com/tour/event/50816"
TEST_TYPE_URL = "https://www.pdga.com/tour/search?date_filter%5Bmin%5D%5Bdate%5D=2021-11-01&date_filter%5Bmax%5D%5Bdate%5D=2021-11-05"


class TestTournamentRawDataRunner(unittest.TestCase):

    def test_should_fail_if_no_arguments(self):
        with self.assertRaises(TypeError):
            handle_arguments([])

    @requests_mock.Mocker()
    def test_should_run_correctly_on_test(self, m):

        mock_correct_urls = [54148, 53900, 54110, 54116, 54253, 54000, 54460, 54583, 53854, 55088, 55076,
                             55030, 55035, 54346, 55016, 54526, 54454, 54427, 54113, 53782, 49924, 49495, 48069]

        for id in mock_correct_urls:
            mock_requests_get(
                f"https://www.pdga.com/tour/event/{id}", TEST_DATA_TOURNAMENT_49356, m)

        mock_requests_get(
            TEST_TYPE_URL, TEST_DATA_TOURNAMENT_LAST_PAGE_TEST, m)

        aws_client = awsClient('s3')
        stubber = Stubber(aws_client)
        for id in mock_correct_urls:
            stubber.add_response(
                'put_object',
                S3_PUT_OBJECT_RESPONSE,
                {'Bucket': 'pdga-project-data',
                    'Key': f'tournament_raw_data/test/{id}.json', 'Body': ANY}
            )
        stubber.activate()

        run_tournament_raw_data("test", aws_client)


if __name__ == '__main__':
    unittest.main()
