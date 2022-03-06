import json
import datetime
from mapping.empty_player_combined_data import EMPTY_PLAYER_COMBINED_DATA

from utils.generalUtils.combine_dictionaries import combine_dictionaries_and_lists
from utils.parsingUtils.combine_data_helpers import (
    combine_player_location,
    combine_player_name
)


class PlayerCombinedData:
    """
    Clean data, combine it from different sources and create new data points.
    """

    def __init__(self, player_parsed_data: json) -> None:
        self.pdga_number = player_parsed_data.get("pdga_number")
        self.status_code = player_parsed_data.get("status_code")
        self.crawl_datetime = player_parsed_data.get("crawl_datetime")
        self.parse_datetime = player_parsed_data.get("parse_datetime")
        self.failed_data_points = player_parsed_data.get(
            "failed_data_points", [])
        self.combine_datetime = datetime.datetime.now()
        self.data = player_parsed_data
        self.combined_data = {**EMPTY_PLAYER_COMBINED_DATA}

    def create_json(self) -> None:
        combined_data = {
            "combine_datetime": str(self.combine_datetime),
            "pdga_number": self.pdga_number,
            "status_code": self.status_code,
            "crawl_datetime": self.crawl_datetime,
            "parse_datetime": self.parse_datetime,
            "failed_data_points": self.failed_data_points
        }

        combine_dictionaries_and_lists(self.combined_data, combined_data)

    def combine_data(self) -> None:
        combine_dictionaries_and_lists(
            self.combined_data, combine_player_name(self.data))
        combine_dictionaries_and_lists(
            self.combined_data, combine_player_location(self.data))

    def analyze_data(self) -> None:
        return
