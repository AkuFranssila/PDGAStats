import unittest

import requests_mock
from player.playerRawDataCrawler import player_raw_data_crawler
from test.data.test_data_pdga_44708 import test_data_pdga_44708
from utils.testUtils.requestsTestUtils import mock_requests_get

class TestPlayerRawDataCrawler(unittest.TestCase):

    @requests_mock.Mocker()
    def test_should_return_raw_data_with_correct_pdga_number(self, m):
        player_id_url = "https://www.pdga.com/player/44708"
        test_data = test_data_pdga_44708
        
        mock_requests_get(player_id_url, test_data, m)
        data = player_raw_data_crawler(44708)

        self.assertEqual(data.pdga_number, 44708)

    @requests_mock.Mocker()
    def test_should_return_raw_data_with_correct_status_code(self, m):
        player_id_url = "https://www.pdga.com/player/44708"
        test_data = test_data_pdga_44708
        
        mock_requests_get(player_id_url, test_data, m)
        data = player_raw_data_crawler(44708)

        self.assertEqual(data.status_code, 200)

    @requests_mock.Mocker()
    def test_should_return_raw_data_with_correct_data(self, m):
        player_id_url = "https://www.pdga.com/player/44708"
        test_data = test_data_pdga_44708
        
        mock_requests_get(player_id_url, test_data, m)
        data = player_raw_data_crawler(44708)

        self.assertEqual(data.raw_data, test_data.get("data"))

    @requests_mock.Mocker()
    def test_should_return_raw_data_with_correct_json_format(self, m):
        player_id_url = "https://www.pdga.com/player/44708"
        test_data = test_data_pdga_44708
        
        mock_requests_get(player_id_url, test_data, m)
        data = player_raw_data_crawler(44708)

        self.assertEqual(data.json_data.keys(), test_data.keys())


if __name__ == '__main__':
    unittest.main()