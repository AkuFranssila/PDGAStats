import unittest
import logging

from player.playerRawData import PlayerRawData
from utils.generalUtils.fileUtils import openJsonFile


class TestPlayerRawData(unittest.TestCase):

    def testShouldInitWithCorrectPdgaNumber(self):
        data = openJsonFile("test/data/testPlayerRawData44708.json")

        playerRawData = PlayerRawData(
            44708,
            data.get("data", ""),
            200
        )

        self.assertEqual(playerRawData.pdgaNumber, 44708)

    def testShouldInitWithCorrectStatusCode(self):
        data = openJsonFile("test/data/testPlayerRawData44708.json")
        playerRawData = PlayerRawData(
            44708,
            data.get("data", ""),
            200
        )

        self.assertEqual(playerRawData.statusCode, 200)

    def testShouldInitWithCorrectRawData(self):
        data = openJsonFile("test/data/testPlayerRawData44708.json")
        playerRawData = PlayerRawData(
            44708,
            data.get("data", ""),
            200
        )

        self.assertEqual(playerRawData.rawData, data.get("data", ""))


if __name__ == '__main__':
    unittest.main()