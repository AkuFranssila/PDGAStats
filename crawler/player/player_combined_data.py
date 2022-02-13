import json
import datetime

from utils.generalUtils.combine_dictionaries import combine_dictionaries_and_lists
from utils.parsingUtils.raw_data_parsers import (
    raw_data_parse_player_career_earnings,
    raw_data_parse_player_career_events_singles,
    raw_data_parse_player_classification,
    raw_data_parse_player_current_rating,
    raw_data_parse_player_current_rating_date,
    raw_data_parse_player_location,
    raw_data_parse_player_location_href,
    raw_data_parse_player_member_since,
    raw_data_parse_player_membership_status,
    raw_data_parse_player_membership_status_expiration_date,
    raw_data_parse_player_name,
    raw_data_parse_player_official_status,
    raw_data_parse_player_official_status_expiration_date,
    raw_data_parse_player_picture_url,
    raw_data_parse_player_singles_wins,
    raw_data_parse_player_upcoming_events,
    raw_data_parse_player_years_played
)


class PlayerCombinedData:
    """
    Collected specific data from raw data without any formatting.
    """

    def __init__(self, player_parsed_data: json) -> None:
        self.pdga_number = player_parsed_data.get("pdga_number")
        self.crawl_datetime = player_raw_data.get("crawl_datetime")
        self.status_code = player_raw_data.get("status_code")
        self.combine_datetime = datetime.datetime.now()
        self.parsed_data = {}

    def create_json(self) -> None:
        parsed_data = {
            "pdga_number": self.pdga_number,
            "crawl_datetime": self.crawl_datetime,
            "parse_datetime": str(self.parse_datetime),
            "status_code": self.status_code,
            "failed_data_points": []
        }

        combine_dictionaries_and_lists(self.parsed_data, parsed_data)

    def parse_raw_data(self) -> None:
        combine_dictionaries_and_lists(
            self.parsed_data, raw_data_parse_player_name(self.raw_data))
        combine_dictionaries_and_lists(
            self.parsed_data, raw_data_parse_player_location(self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data,
                                       raw_data_parse_player_location_href(self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data,
                                       raw_data_parse_player_classification(self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data,
                                       raw_data_parse_player_member_since(self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data, raw_data_parse_player_membership_status(
            self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data, raw_data_parse_player_membership_status_expiration_date(
            self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data, raw_data_parse_player_official_status(
            self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data, raw_data_parse_player_official_status_expiration_date(
            self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data,
                                       raw_data_parse_player_current_rating(self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data, raw_data_parse_player_current_rating_date(
            self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data, raw_data_parse_player_career_events_singles(
            self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data,
                                       raw_data_parse_player_singles_wins(self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data, raw_data_parse_player_career_earnings(
            self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data, raw_data_parse_player_upcoming_events(
            self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data,
                                       raw_data_parse_player_years_played(self.raw_data))
        combine_dictionaries_and_lists(self.parsed_data,
                                       raw_data_parse_player_picture_url(self.raw_data))
