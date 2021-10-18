import datetime
import json

class PlayerRawData:
    """
    Creates an object that stores raw data of the crawled player. 

    This data can be saved to S3 or locally.
    """
    def __init__(self, pdgaNumber: int, rawData: str, statusCode: int) -> None:
        self.pdgaNumber = pdgaNumber
        self.crawlDateTime = datetime.datetime.now()
        self.rawData = rawData
        self.statusCode = statusCode
        self.jsonData = None

    def createJson(self) -> None:
        jsonData = {
            'pdgaNumber': str(self.pdgaNumber),
            'crawlDateTime': str(self.crawlDateTime),
            'data': str(self.rawData),
            'statusCode': str(self.statusCode)
        }

        self.jsonData = jsonData

    def printJson(self) -> None:
        print(json.dumps(self.jsonData, indent=4))
