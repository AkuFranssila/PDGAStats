from typing import Tuple
from player.playerRawData import PlayerRawData
from utils.s3Utils.uploadUtils import upload_object_s3
import logging
import requests
import argparse

logging.getLogger().setLevel("INFO")

def handle_arguments() -> Tuple:
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument(
        '--pdga_number',
        type=int,
        required=True,
        help="PDGA Number that needs to be crawled."
        )

    argumentParser.add_argument(
        '--crawl_count',
        type=str,
        default="test",
        help="Sub folder where the data should be uploaded. crawl_count is a unique folder name used to specify which crawl count is going on. Use test if unknown"
        )

    pdga_number: int = argumentParser.parse_args().pdga_number
    crawl_count: str =  argumentParser.parse_args().crawl_count

    return pdga_number, crawl_count


def player_raw_data_crawler(pdga_number: int) -> PlayerRawData:
    url = f"https://www.pdga.com/player/{str(pdga_number)}"
    response = requests.get(url)
    data = response.text
    status_code = response.status_code

    player_raw_data = PlayerRawData(pdga_number, data, status_code)
    player_raw_data.create_json()

    return player_raw_data
    

if __name__ == "__main__":
    pdga_number, crawl_count = handle_arguments()
    player_raw_data = player_raw_data_crawler(pdga_number)
    player_raw_data.create_json()
    upload_object_s3("player_raw_data", crawl_count, str(player_raw_data.pdga_number), '', player_raw_data.json_data)
    player_raw_data.printJson()