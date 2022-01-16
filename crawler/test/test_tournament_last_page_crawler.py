import unittest
import requests_mock

from player.playerLatestIdCrawler import player_latest_id_crawler
from utils.testUtils.requestsTestUtils import mock_requests_get
from test.data.test_data_latest_id_202725 import TEST_DATA_LATEST_ID_202725


class TestTournamentLastPageCrawler(unittest.TestCase):
    @requests_mock.Mocker()
    def test_should_get_latest_id_correctly(self, m):
        test_url = "https://www.pdga.com/players?FirstName=&LastName=&PDGANum=&Status=All&Class=All&MemberType=All&City=&StateProv=All&Country=All&Country_1=All&UpdateDate=&order=PDGANum&sort=desc"
        test_json = TEST_DATA_LATEST_ID_202725
        mock_requests_get(test_url, test_json, m)
        latest_id = player_latest_id_crawler()
        self.assertEqual(latest_id, 202725)

    @requests_mock.Mocker()
    def test_should_return_id_as_integer(self, m):
        test_url = "https://www.pdga.com/players?FirstName=&LastName=&PDGANum=&Status=All&Class=All&MemberType=All&City=&StateProv=All&Country=All&Country_1=All&UpdateDate=&order=PDGANum&sort=desc"
        test_json = TEST_DATA_LATEST_ID_202725
        mock_requests_get(test_url, test_json, m)
        latest_id = player_latest_id_crawler()
        self.assertTrue(isinstance(latest_id, int))


if __name__ == '__main__':
    unittest.main()
