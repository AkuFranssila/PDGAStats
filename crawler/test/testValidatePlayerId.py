import unittest
import logging

from utils.crawlingUtils.validatePlayerId import validate_player_id


class TestValidatePlayerId(unittest.TestCase):

    def test_should_succeed_if_id_over_150k(self):
        test_id = "151000"

        test_id = validate_player_id(test_id)
        self.assertEqual(test_id, 151_000)

    def test_should_raise_error_if_id_under_150k(self):
        with self.assertRaises(Exception):
            test_id = "44000"
            test_id = validate_player_id(test_id)

    def test_should_convert_string_to_int(self):
        test_id = "151000"

        test_id = validate_player_id(test_id)
        self.assertTrue(isinstance(test_id, int))

    def test_should_fail_if_cant_be_converted_to_int(self):
        with self.assertRaises(Exception):
            test_id = "TEST"
            test_id = validate_player_id(test_id)

    def test_should_have_correct_error_message_for_not_int(self):
        with self.assertRaises(Exception) as error_message:
            test_id = "TEST"
            test_id = validate_player_id(test_id)
            logging.debug(error_message.exception)
            self.assertTrue(
                "Player ID can not be converted to INT. Check crawler for problems." in error_message.exception)

    def test_should_have_correct_error_message_for_too_low_id(self):
        with self.assertRaises(Exception) as error_message:
            test_id = "44000"
            test_id = validate_player_id(test_id)
            logging.debug(error_message.exception)
            self.assertTrue(
                "Player ID is too low to be valid. Check crawler for problems." in error_message.exception)


if __name__ == '__main__':
    unittest.main()
