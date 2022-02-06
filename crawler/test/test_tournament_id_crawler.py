import unittest
import requests_mock
from tournament.tournament_id_crawler import tournament_id_crawler
from utils.testUtils.requestsTestUtils import mock_requests_get

from test.data.test_data_tournament_id_page_1 import TEST_DATA_TOURNAMENT_ID_PAGE_1
from test.data.test_data_tournament_id_page_2 import TEST_DATA_TOURNAMENT_ID_PAGE_2
from test.data.test_data_tournament_last_page_test import TEST_DATA_TOURNAMENT_LAST_PAGE_TEST

tournament_latest_id_search_url = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-12-01&date_filter[max][date]=2021-12-04"
tournament_latest_id_page_1 = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-12-01&date_filter[max][date]=2021-12-04&page=0"
tournament_latest_id_page_2 = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-12-01&date_filter[max][date]=2021-12-04&page=1"

tournament_latest_id_single_page_search_url = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-11-01&date_filter[max][date]=2021-11-05"
tournament_latest_id_single_page_1 = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-11-01&date_filter[max][date]=2021-11-05&page=0"


class TestTournamentLastPageCrawler(unittest.TestCase):
    @requests_mock.Mocker()
    def test_should_return_correct_ids_when_multiple_pages(self, m):
        mock_correct_urls = [54805, 55382, 55574, 55571, 54988, 53592, 48420, 55627, 55622, 55567, 55546, 55539, 55522, 55437, 55280, 55271, 55200, 55134, 55091, 54975, 54973, 54965, 54952,
                             54938, 54862, 54824, 54771, 54722, 54713, 54682, 54650, 54634, 54557, 54542, 54538, 54345, 53872, 53198, 53017, 52954, 52668, 51173, 49734, 48921, 48409, 48089]

        mock_requests_get(tournament_latest_id_search_url,
                          TEST_DATA_TOURNAMENT_ID_PAGE_1, m)
        mock_requests_get(tournament_latest_id_page_1,
                          TEST_DATA_TOURNAMENT_ID_PAGE_1, m)
        mock_requests_get(tournament_latest_id_page_2,
                          TEST_DATA_TOURNAMENT_ID_PAGE_2, m)
        parsed_urls = tournament_id_crawler(tournament_latest_id_search_url)
        self.assertEqual(parsed_urls, mock_correct_urls)
        self.assertEqual(len(parsed_urls), 46)

    @requests_mock.Mocker()
    def test_should_return_correct_ids_when_single_page(self, m):
        mock_correct_urls = [54148, 53900, 54110, 54116, 54253, 54000, 54460, 54583, 53854, 55088, 55076,
                             55030, 55035, 54346, 55016, 54526, 54454, 54427, 54113, 53782, 49924, 49495, 48069]

        mock_requests_get(tournament_latest_id_single_page_search_url,
                          TEST_DATA_TOURNAMENT_LAST_PAGE_TEST, m)
        mock_requests_get(tournament_latest_id_single_page_1,
                          TEST_DATA_TOURNAMENT_LAST_PAGE_TEST, m)
        parsed_urls = tournament_id_crawler(
            tournament_latest_id_single_page_search_url)
        self.assertEqual(parsed_urls, mock_correct_urls)
        self.assertEqual(len(parsed_urls), 23)


if __name__ == '__main__':
    unittest.main()
