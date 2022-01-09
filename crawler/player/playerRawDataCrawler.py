from typing import Tuple
from player.playerRawData import PlayerRawData
from utils.s3Utils.uploadUtils import uploadObjectS3
import logging
import requests
import argparse

logging.getLogger().setLevel("INFO")

def handleArguments() -> Tuple:
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument(
        '--pdgaNumber',
        type=int,
        required=True,
        help="PDGA Number that needs to be crawled."
        )

    argumentParser.add_argument(
        '--crawlCount',
        type=str,
        default="test",
        help="Sub folder where the data should be uploaded. crawlCount is a unique folder name used to specify which crawl count is going on. Use test if unknown"
        )

    pdgaNumber: int = argumentParser.parse_args().pdgaNumber
    crawlCount: str =  argumentParser.parse_args().crawlCount

    return pdgaNumber, crawlCount


def playerRawDataCrawler(pdgaNumber: int) -> PlayerRawData:
    url = f"https://www.pdga.com/player/{str(pdgaNumber)}"
    response = requests.get(url)
    data = response.text
    statusCode = response.status_code

    playerRawData = PlayerRawData(pdgaNumber, data, statusCode)
    playerRawData.createJson()

    return playerRawData
    

if __name__ == "__main__":
    pdgaNumber, crawlCount = handleArguments()
    playerRawData = playerRawDataCrawler(pdgaNumber)
    playerRawData.createJson()
    uploadObjectS3("PlayerRawData", crawlCount, str(playerRawData.pdgaNumber), '', playerRawData.jsonData)
    playerRawData.printJson()