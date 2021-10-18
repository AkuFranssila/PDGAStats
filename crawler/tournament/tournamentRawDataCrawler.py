from typing import Tuple
from tournament.tournamentRawData import TournamentRawData
from utils.s3Utils.uploadUtils import uploadObjectS3
import logging
import requests
import argparse

logging.getLogger().setLevel("INFO")

def handleArguments() -> Tuple:
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument(
        '--tournamentId',
        type=int,
        required=True,
        help="Tournament ID that needs to be crawled."
        )

    argumentParser.add_argument(
        '--crawlCount',
        type=str,
        default="test",
        help="Sub folder where the data should be uploaded. crawlCount is a unique folder name used to specify which crawl count is going on. Use test if unknown"
        )

    tournamentId: int = argumentParser.parse_args().tournamentId
    crawlCount: str =  argumentParser.parse_args().crawlCount

    return tournamentId, crawlCount


def tournamentRawDataCrawler(tournamentId: int) -> TournamentRawData:
    url = f"https://www.pdga.com/tour/event/{str(tournamentId)}"
    response = requests.get(url)
    data = response.text
    statusCode = response.status_code

    tournamentRawData = TournamentRawData(tournamentId, data, statusCode)

    return tournamentRawData
    

if __name__ == "__main__":
    tournamentId, crawlCount = handleArguments()
    tournamentRawData = tournamentRawDataCrawler(tournamentId)
    tournamentRawData.createJson()
    uploadObjectS3("TournamentRawData", crawlCount, str(tournamentRawData.tournamentId), '', tournamentRawData.jsonData)
    tournamentRawData.printJson()