import unittest

from tournament.tournament_raw_data import TournamentRawData
from test.data.test_data_tournament_49356 import TEST_DATA_TOURNAMENT_49356


class TestTournamentRawData(unittest.TestCase):

    def test_should_init_with_correct_tournament_id(self):
        data = TEST_DATA_TOURNAMENT_49356

        tournament_raw_data = TournamentRawData(
            49356,
            data.get("data", ""),
            200
        )

        self.assertEqual(tournament_raw_data.tournament_id, 49356)

    def test_should_init_with_correct_status_code(self):
        data = TEST_DATA_TOURNAMENT_49356
        tournament_raw_data = TournamentRawData(
            49356,
            data.get("data", ""),
            200
        )

        self.assertEqual(tournament_raw_data.status_code, 200)

    def test_should_init_with_correct_data(self):
        data = TEST_DATA_TOURNAMENT_49356
        tournament_raw_data = TournamentRawData(
            49356,
            data.get("data", ""),
            200
        )

        self.assertEqual(tournament_raw_data.raw_data, data.get("data", ""))


if __name__ == '__main__':
    unittest.main()
