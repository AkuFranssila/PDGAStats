import unittest
import logging

from tournament.tournamentRawData import TournamentRawData
from test.data.test_data_tournament_49356 import test_data_tournament_49356


class TestTournamentRawData(unittest.TestCase):

    def test_should_init_with_correct_tournament_id(self):
        data = test_data_tournament_49356

        tournament_raw_data = TournamentRawData(
            49356,
            data.get("data", ""),
            200
        )

        self.assertEqual(tournament_raw_data.tournamentId, 49356)

    def test_should_init_with_correct_status_code(self):
        data = test_data_tournament_49356
        tournamentRawData = TournamentRawData(
            49356,
            data.get("data", ""),
            200
        )

        self.assertEqual(tournamentRawData.tournamentId, 49356)


if __name__ == '__main__':
    unittest.main()