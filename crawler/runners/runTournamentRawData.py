from typing import Tuple

from player.playerRawData import PlayerRawData
from player.playerLatestIdCrawler import player_latest_id_crawler
from player.playerRawDataCrawler import player_raw_data_crawler

from utils.s3Utils.uploadUtils import upload_object_s3
from utils.s3Utils.findSubFolderCount import find_sub_folder_count

import logging
import argparse

logging.getLogger().setLevel("INFO")


def handle_arguments() -> Tuple:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        '--type',
        type=str,
        required=True,
        default="test",
        help="Select to crawl all or test and define custom start and end id"
    )

    argument_parser.add_argument(
        '--start_id',
        type=int,
        help="Start ID if test crawl"
    )

    argument_parser.add_argument(
        '--end_id',
        type=int,
        help="End ID if test crawl"
    )

    type: str = argument_parser.parse_args().type
    start_id: int = argument_parser.parse_args().start_id
    end_id: int = argument_parser.parse_args().end_id

    return type, start_id, end_id


def run_player_raw_data(type: str, start_id: int, end_id: int) -> None:
    if (type == "all"):
        start_id = 1
        end_id = player_latest_id_crawler()
        crawl_count = find_sub_folder_count()
    else:
        crawl_count = "test"

    for i in range(start_id, end_id + 1):
        player_raw_data = player_raw_data_crawler(i)
        player_raw_data.create_json()
        upload_object_s3("player_raw_data", crawl_count, str(
            player_raw_data.pdga_number), '', player_raw_data.json_data)


if __name__ == "__main__":
    type, start_id, end_id = handle_arguments()
    run_player_raw_data(type, start_id, end_id)
