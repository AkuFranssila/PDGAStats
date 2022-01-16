import unittest
import logging
from test.data.test_data_pdga_44708 import TEST_DATA_PDGA_44708

from player.playerRawData import PlayerRawData


class TestPlayerRawData(unittest.TestCase):

    def test_should_init_with_correct_pdga_number(self):
        data = TEST_DATA_PDGA_44708

        player_raw_data = PlayerRawData(
            44708,
            data.get("data", ""),
            200
        )

        self.assertEqual(player_raw_data.pdga_number, 44708)

    def test_should_init_with_correct_status_code(self):
        data = TEST_DATA_PDGA_44708
        player_raw_data = PlayerRawData(
            44708,
            data.get("data", ""),
            200
        )

        self.assertEqual(player_raw_data.status_code, 200)

    def test_should_init_with_correct_raw_data(self):
        data = TEST_DATA_PDGA_44708
        player_raw_data = PlayerRawData(
            44708,
            data.get("data", ""),
            200
        )

        self.assertEqual(player_raw_data.raw_data, data.get("data", ""))


if __name__ == '__main__':
    unittest.main()
