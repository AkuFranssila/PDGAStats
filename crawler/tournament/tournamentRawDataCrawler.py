from typing import Tuple
from tournament.tournamentRawData import TournamentRawData
from utils.s3Utils.uploadUtils import upload_object_s3
import logging
import requests
import argparse
import json

logging.getLogger().setLevel("INFO")


def handle_arguments() -> Tuple:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        '--tournament_id',
        type=int,
        required=True,
        help="Tournament ID that needs to be crawled."
    )

    argument_parser.add_argument(
        '--crawl_count',
        type=str,
        default="test",
        help="Sub folder where the data should be uploaded. crawlCount is a unique folder name used to specify which crawl count is going on. Use test if unknown"
    )

    tournament_id: int = argument_parser.parse_args().tournament_id
    crawl_count: str = argument_parser.parse_args().crawl_count

    return tournament_id, crawl_count


def tournament_raw_data_crawler(tournament_id: int) -> TournamentRawData:
    url = f"https://www.pdga.com/tour/event/{str(tournament_id)}"
    response = requests.get(url)
    data = response.text
    status_code = response.status_code

    tournament_raw_data = TournamentRawData(tournament_id, data, status_code)

    return tournament_raw_data


if __name__ == "__main__":
    tournament_id, crawl_count = handle_arguments()
    tournament_raw_data = tournament_raw_data_crawler(tournament_id)
    tournament_raw_data.create_json()
    upload_object_s3("tournament_raw_data", crawl_count, str(
        tournament_raw_data.tournament_id), '', tournament_raw_data.json_data)
    tournament_raw_data.print_json()
