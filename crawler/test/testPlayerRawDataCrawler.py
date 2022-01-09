import unittest

import requests_mock
from player.playerRawDataCrawler import playerRawDataCrawler
from test.data.test_data_pdga_44708 import test_data_pdga_44708
from utils.testUtils.requestsTestUtils import mock_requests_get

class TestPlayerRawDataCrawler(unittest.TestCase):

    @requests_mock.Mocker()
    def testShouldReturnRawDataWithCorrectPdgaNumber(self, m):
        player_id_url = "https://www.pdga.com/player/44708"
        test_data = test_data_pdga_44708
        
        mock_requests_get(player_id_url, test_data, m)
        data = playerRawDataCrawler(44708)

        self.assertEqual(data.pdgaNumber, 44708)

    @requests_mock.Mocker()
    def testShouldReturnRawDataWithCorrectStatusCode(self, m):
        player_id_url = "https://www.pdga.com/player/44708"
        test_data = test_data_pdga_44708
        
        mock_requests_get(player_id_url, test_data, m)
        data = playerRawDataCrawler(44708)

        self.assertEqual(data.statusCode, 200)

    @requests_mock.Mocker()
    def testShouldReturnRawDataWithCorrectData(self, m):
        player_id_url = "https://www.pdga.com/player/44708"
        test_data = test_data_pdga_44708
        
        mock_requests_get(player_id_url, test_data, m)
        data = playerRawDataCrawler(44708)

        self.assertEqual(data.rawData, test_data.get("data"))

    @requests_mock.Mocker()
    def testShouldReturnRawDataWithCorrectJsonFormat(self, m):
        player_id_url = "https://www.pdga.com/player/44708"
        test_data = test_data_pdga_44708
        
        mock_requests_get(player_id_url, test_data, m)
        data = playerRawDataCrawler(44708)

        self.assertEqual(data.jsonData.keys(), test_data.keys())


if __name__ == '__main__':
    unittest.main()