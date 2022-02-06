from distutils.log import error
import unittest
import logging

from utils.crawlingUtils.parse_tournament_id import parse_tournament_id


TEST_ID_FULL = "https://www.pdga.com/tour/event/50816"
TEST_ID_FULL_WITH_PARAMETERS = "https://www.pdga.com/tour/event/50816?trackingId=XXXX&anotherId=TESTEST"
TEST_ID_GLOBAL_EVENT = "https://www.pdga.com/women/global-event/results/2021"
TEST_ID_SHORT = "/tour/event/50816"
TEST_ID_INVALID = "/tour/event/JJSKKDKDKDK"


class TestValidatePlayerId(unittest.TestCase):
    def test_should_return_int(self):
        tournament_id = parse_tournament_id(TEST_ID_FULL)
        self.assertTrue(isinstance(tournament_id, int))

    def test_should_parse_from_full_url(self):
        tournament_id = parse_tournament_id(TEST_ID_FULL)
        self.assertEqual(tournament_id, 50816)

    def test_should_parse_from_full_url_with_parameters(self):
        tournament_id = parse_tournament_id(TEST_ID_FULL_WITH_PARAMETERS)
        self.assertEqual(tournament_id, 50816)

    def test_should_parse_from_short_url(self):
        tournament_id = parse_tournament_id(TEST_ID_SHORT)
        self.assertEqual(tournament_id, 50816)

    def test_should_fail_on_global_event_urls(self):
        self.maxDiff = None

        with self.assertRaises(Exception) as error_message:
            parse_tournament_id(TEST_ID_GLOBAL_EVENT)

        self.assertEqual(str(error_message.exception), str(Exception(
            "Incorrect tournament URL. Tournament URL did not contain tour/event/.")))

    def test_should_fail_on_invalid_urls(self):
        self.maxDiff = None
        with self.assertRaises(Exception) as error_message:
            parse_tournament_id(TEST_ID_INVALID)

        self.assertEqual(str(error_message.exception), str(Exception(
            "Parsed tournament ID was not convertable to INT. Check tournament ID.")))


if __name__ == '__main__':
    unittest.main()
