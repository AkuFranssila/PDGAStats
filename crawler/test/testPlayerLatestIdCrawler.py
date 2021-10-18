import unittest
import responses

from player.playerLatestIdCrawler import playerLatestIdCrawler

from utils.testUtils.requestsTestUtils import mockRequestsGet
from utils.generalUtils.fileUtils import openJsonFile

@responses.activate
class TestPlayerLatestIdCrawler(unittest.TestCase):
    playerIdUrl = "https://www.pdga.com/players?FirstName=&LastName=&PDGANum=&Status=All&Class=All&MemberType=All&City=&StateProv=All&Country=All&Country_1=All&UpdateDate=&order=PDGANum&sort=desc"
    testData = openJsonFile("test/data/latestIdRawData.json")
    mockRequestsGet(playerIdUrl, testData, 200)

    def testShouldCrawlLatestIdCorrectly(self):
        latestId = playerLatestIdCrawler()
        self.assertEqual(latestId, 193393)

    def testLatestIdShouldBeInt(self):
        latestId = playerLatestIdCrawler()
        self.assertTrue(isinstance(latestId, int))

if __name__ == '__main__':
    unittest.main()