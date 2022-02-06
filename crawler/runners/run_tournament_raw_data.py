from typing import Tuple
from utils.crawlingUtils.tournament_date_options import tournament_date_options

from tournament.tournament_id_crawler import tournament_id_crawler
from tournament.tournament_raw_data_crawler import tournament_raw_data_crawler

from utils.s3Utils.uploadUtils import upload_object_s3
from utils.s3Utils.findSubFolderCount import find_sub_folder_count
from utils.s3Utils.client import awsClient

from utils.generalUtils.notification_utils import print_process_notification

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

    crawl_type: str = argument_parser.parse_args().type

    return crawl_type


def run_tournament_raw_data(type: str, aws_client: any) -> None:
    tournament_list_url = tournament_date_options(type)
    tournament_ids = tournament_id_crawler(tournament_list_url)

    if (type == "test"):
        crawl_count = "test"
    else:
        crawl_count = find_sub_folder_count("tournament_raw_data", aws_client)

    for count, i in enumerate(tournament_ids):
        print_process_notification(count, len(tournament_ids))
        tournament_raw_data = tournament_raw_data_crawler(i)
        tournament_raw_data.create_json()
        upload_object_s3("tournament_raw_data", crawl_count, str(
            tournament_raw_data.tournament_id), '', tournament_raw_data.json_data, aws_client)


if __name__ == "__main__":
    crawl_type = handle_arguments()
    run_tournament_raw_data(crawl_type, awsClient('s3'))
