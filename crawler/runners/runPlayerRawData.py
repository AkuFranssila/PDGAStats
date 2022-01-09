from typing import Tuple

from player.playerRawData import PlayerRawData
from player.playerLatestIdCrawler import playerLatestIdCrawler
from player.playerRawDataCrawler import playerRawDataCrawler

from utils.s3Utils.uploadUtils import uploadObjectS3
from utils.s3Utils.findSubFolderCount import findSubFolderCount

import logging
import argparse

logging.getLogger().setLevel("INFO")

def handleArguments() -> Tuple:
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument(
        '--type',
        type=str,
        required=True,
        default="test",
        help="Select to crawl all or test and define custom start and end id"
        )

    argumentParser.add_argument(
        '--startId',
        type=int,
        help="Start ID if test crawl"
        )

    argumentParser.add_argument(
        '--endId',
        type=int,
        help="End ID if test crawl"
        )

    type: str = argumentParser.parse_args().type
    startId: int = argumentParser.parse_args().startId
    endId: int = argumentParser.parse_args().endId

    return type, startId, endId


def runPlayerRawData(type: str, startId: int, endId: int) -> None:
    if (type == "all"):
        startId = 1
        endId = playerLatestIdCrawler()
        crawlCount = findSubFolderCount("playerRawData")
    else:
        crawlCount = "test"

    for i in range(startId, endId + 1):
        playerRawData = playerRawDataCrawler(i)
        playerRawData.createJson()
        uploadObjectS3("PlayerRawData", crawlCount, str(playerRawData.pdgaNumber), '', playerRawData.jsonData)
    

if __name__ == "__main__":
    type, startId, endId = handleArguments()
    runPlayerRawData(type, startId, endId)
