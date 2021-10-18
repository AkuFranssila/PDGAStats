import unittest
import logging

from utils.crawlingUtils.validatePlayerId import validatePlayerId

class TestValidatePlayerId(unittest.TestCase):

    def testShouldValidateIdIfOver150k(self):
        testId = "151000"

        testId = validatePlayerId(testId)
        self.assertEqual(testId, 151_000)

    def testShouldRaiseErrorIfUnder150k(self):
        with self.assertRaises(Exception):
            testId = "44000"
            testId = validatePlayerId(testId)

    def testShouldConvertStringToInt(self):
        testId = "151000"

        testId = validatePlayerId(testId)
        self.assertTrue(isinstance(testId, int))

    def testShouldFailIfNotConvertableToInt(self):
        with self.assertRaises(Exception):
            testId = "TEST"
            testId = validatePlayerId(testId)

    def testShouldHaveCorrectErrorMessageForNotInt(self):
        with self.assertRaises(Exception) as errorMsg:
            testId = "TEST"
            testId = validatePlayerId(testId)
            logging.debug(errorMsg.exception)
            self.assertTrue("Player ID can not be converted to INT. Check crawler for problems." in errorMsg.exception)

    def testShouldHaveCorrectErrorMessageForTooLowId(self):
        with self.assertRaises(Exception) as errorMsg:
            testId = "44000"
            testId = validatePlayerId(testId)
            logging.debug(errorMsg.exception)
            self.assertTrue("Player ID is too low to be valid. Check crawler for problems." in errorMsg.exception)


if __name__ == '__main__':
    unittest.main()