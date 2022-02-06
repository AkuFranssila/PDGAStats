import unittest

import requests_mock
from tournament.tournament_raw_data_crawler import tournament_raw_data_crawler
from test.data.test_data_tournament_49356 import TEST_DATA_TOURNAMENT_49356
from utils.testUtils.requestsTestUtils import mock_requests_get


TOURNAMENT_49356_URL = "https://www.pdga.com/tour/event/49356"


class TestTournamentRawDataCrawler(unittest.TestCase):

    @requests_mock.Mocker()
    def test_should_return_raw_data_with_correct_tournament_id(self, m):
        mock_requests_get(TOURNAMENT_49356_URL, TEST_DATA_TOURNAMENT_49356, m)
        data = tournament_raw_data_crawler(49356)
        self.assertEqual(data.tournament_id, 49356)

    @requests_mock.Mocker()
    def test_should_return_raw_data_with_correct_status_code(self, m):
        mock_requests_get(TOURNAMENT_49356_URL, TEST_DATA_TOURNAMENT_49356, m)
        data = tournament_raw_data_crawler(49356)
        self.assertEqual(data.status_code, 200)

    @requests_mock.Mocker()
    def test_should_return_raw_data_with_correct_data(self, m):
        mock_requests_get(TOURNAMENT_49356_URL, TEST_DATA_TOURNAMENT_49356, m)
        data = tournament_raw_data_crawler(49356)
        self.assertEqual(data.raw_data, TEST_DATA_TOURNAMENT_49356.get("data"))

    @requests_mock.Mocker()
    def test_should_return_raw_data_with_correct_json_format(self, m):
        mock_requests_get(TOURNAMENT_49356_URL, TEST_DATA_TOURNAMENT_49356, m)
        data = tournament_raw_data_crawler(49356)
        self.assertEqual(data.json_data.keys(),
                         TEST_DATA_TOURNAMENT_49356.keys())


if __name__ == '__main__':
    unittest.main()
