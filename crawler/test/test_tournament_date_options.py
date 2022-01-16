import unittest
import time_machine
import datetime

from utils.crawlingUtils.tournament_date_options import tournament_date_options


class TestTournamentDateOptions(unittest.TestCase):
    def test_should_return_correct_url_for_all(self):
        with time_machine.travel(datetime.datetime(2022, 1, 15)):
            correct_url = "https://www.pdga.com/tour/search?date_filter[min][date]=1979-01-01&date_filter[max][date]=2022-12-31"
            tournament_last_page_url = tournament_date_options('all')
            self.assertEqual(tournament_last_page_url, correct_url)

    def test_should_return_correct_url_for_latest(self):
        with time_machine.travel(datetime.datetime(2022, 1, 15)):
            correct_url = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-11-15&date_filter[max][date]=2022-12-31"
            tournament_last_page_url = tournament_date_options('latest')
            self.assertEqual(tournament_last_page_url, correct_url)

    def test_should_return_correct_url_for_test(self):
        with time_machine.travel(datetime.datetime(2022, 1, 15)):
            correct_url = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-11-01&date_filter[max][date]=2021-11-05"
            tournament_last_page_url = tournament_date_options('test')
            self.assertEqual(tournament_last_page_url, correct_url)

    def test_should_return_error_if_incorrect_option(self):
        with self.assertRaises(Exception) as error_message:
            tournament_date_options('BLAABLAA')
            self.assertTrue(
                "Incorrect Tournament Crawl Options. Select all, test or latest." in error_message.exception)


if __name__ == '__main__':
    unittest.main()
