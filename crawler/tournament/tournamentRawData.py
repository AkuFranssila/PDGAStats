import datetime
import json

class TournamentRawData:
    """
    Creates an object that stores raw data of the crawled tournament. 

    This data can be saved to S3 or locally.
    """
    def __init__(self, tournamentId: int, rawData: str, statusCode: int) -> None:
        self.tournamentId = tournamentId
        self.crawlDateTime = datetime.datetime.now()
        self.rawData = rawData
        self.statusCode = statusCode
        self.jsonData = None

    def createJson(self) -> None:
        jsonData = {
            'tournamentId': str(self.tournamentId),
            'crawlDateTime': str(self.crawlDateTime),
            'data': str(self.rawData),
            'statusCode': str(self.statusCode)
        }

        self.jsonData = jsonData

    def printJson(self) -> None:
        print(json.dumps(self.jsonData, indent=4))
