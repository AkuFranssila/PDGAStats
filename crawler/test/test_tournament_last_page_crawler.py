import unittest
import requests_mock
from test.data.test_data_tournament_last_page_all import TEST_DATA_TOURNAMENT_LAST_PAGE_ALL
from test.data.test_data_tournament_last_page_latest import TEST_DATA_TOURNAMENT_LAST_PAGE_LATEST
from test.data.test_data_tournament_last_page_test import TEST_DATA_TOURNAMENT_LAST_PAGE_TEST
from tournament.tournament_last_page_crawler import tournament_last_page_crawler

from utils.testUtils.requestsTestUtils import mock_requests_get
from test.data.test_data_latest_id_202725 import TEST_DATA_LATEST_ID_202725

latest_option_url = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-11-15&date_filter[max][date]=2022-12-31"
test_option_url = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-11-01&date_filter[max][date]=2021-11-05"
all_option_url = "https://www.pdga.com/tour/search?date_filter[min][date]=1979-01-01&date_filter[max][date]=2022-12-31"

latest_option_test_json = TEST_DATA_TOURNAMENT_LAST_PAGE_LATEST
test_option_test_json = TEST_DATA_TOURNAMENT_LAST_PAGE_TEST
all_option_test_json = TEST_DATA_TOURNAMENT_LAST_PAGE_ALL


class TestTournamentLastPageCrawler(unittest.TestCase):
    @requests_mock.Mocker()
    def test_should_return_id_as_integer(self, m):
        mock_requests_get(test_option_url, test_option_test_json, m)
        last_page_number = tournament_last_page_crawler(test_option_url)
        self.assertTrue(isinstance(last_page_number, int))

    @requests_mock.Mocker()
    def test_should_get_correct_last_page_for_test_option(self, m):
        mock_requests_get(test_option_url, test_option_test_json, m)
        last_page_number = tournament_last_page_crawler(test_option_url)
        self.assertEqual(last_page_number, 1)

    @requests_mock.Mocker()
    def test_should_get_correct_last_page_for_all_option(self, m):
        mock_requests_get(all_option_url, all_option_test_json, m)
        last_page_number = tournament_last_page_crawler(all_option_url)
        self.assertEqual(last_page_number, 2029)

    @requests_mock.Mocker()
    def test_should_return_all_option_in_correct_range(self, m):
        mock_requests_get(all_option_url, all_option_test_json, m)
        last_page_number = tournament_last_page_crawler(all_option_url)
        self.assertGreater(last_page_number, 1500)

    @requests_mock.Mocker()
    def test_should_get_correct_last_page_for_latest_option(self, m):
        mock_requests_get(latest_option_url, latest_option_test_json, m)
        last_page_number = tournament_last_page_crawler(latest_option_url)
        self.assertEqual(last_page_number, 104)

    @requests_mock.Mocker()
    def test_should_return_latest_option_in_correct_range(self, m):
        mock_requests_get(latest_option_url, latest_option_test_json, m)
        last_page_number = tournament_last_page_crawler(latest_option_url)
        self.assertGreater(last_page_number, 100)


if __name__ == '__main__':
    unittest.main()
