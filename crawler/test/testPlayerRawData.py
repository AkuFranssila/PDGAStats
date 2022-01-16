import unittest
import logging

from player.playerRawData import PlayerRawData
from utils.generalUtils.fileUtils import open_json_file


class TestPlayerRawData(unittest.TestCase):

    def test_should_init_with_correct_pdga_number(self):
        data = open_json_file("test/data/testPlayerRawData44708.json")

        player_raw_data = PlayerRawData(
            44708,
            data.get("data", ""),
            200
        )

        self.assertEqual(player_raw_data.pdga_number, 44708)

    def test_should_init_with_correct_status_code(self):
        data = open_json_file("test/data/testPlayerRawData44708.json")
        player_raw_data = PlayerRawData(
            44708,
            data.get("data", ""),
            200
        )

        self.assertEqual(player_raw_data.status_code, 200)

    def test_should_init_with_correct_raw_data(self):
        data = open_json_file("test/data/testPlayerRawData44708.json")
        player_raw_data = PlayerRawData(
            44708,
            data.get("data", ""),
            200
        )

        self.assertEqual(player_raw_data.raw_data, data.get("data", ""))


if __name__ == '__main__':
    unittest.main()
