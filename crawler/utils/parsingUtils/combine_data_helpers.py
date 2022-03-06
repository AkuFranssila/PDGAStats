import json
from utils.parsingUtils.clean_string import clean_string
import pycountry

from mapping.stateMapping import US_STATES_DICT_REVERSED
from utils.generalUtils.regex_utils import find_first_middle_last_names, find_locations_from_href
from utils.parsingUtils.clean_pdga_errors import clean_pdga_errors


def combine_player_name(data) -> json:
    """
    Cleans the player name data and splits the name to first, middle and last names.
    """

    combined_data_point = {
        "player_name": None,
        "player_first_name": None,
        "player_middle_name": None,
        "player_last_name": None
    }

    if (data.get("player_name")):
        player_name = data.get("player_name").split('#')[0].strip()
        names = find_first_middle_last_names(player_name)
        combined_data_point["player_name"] = player_name
        combined_data_point.update(names)

    return combined_data_point


def combine_player_location(data) -> json:
    """
    Takes the player location and location href fields and splits the location to own fields.
    """

    combined_data_point = {
        "player_location": None,
        "player_country": None,
        "player_country_short": None,
        "player_state": None,
        "player_state_short": None,
        "player_city": None
    }

    player_location_href = data.get("player_location_href")
    player_location = data.get("player_location")

    if (player_location_href):
        href_locations = find_locations_from_href(player_location_href)

        country_short = href_locations.get("player_country_short")
        state_short = href_locations.get("player_state_short")
        city = href_locations.get("player_city")

        if (country_short):
            href_locations["player_country"] = pycountry.countries.get(
                alpha_2=country_short).name

        if (state_short):
            href_locations["player_state"] = US_STATES_DICT_REVERSED.get(
                state_short)

        if (city):
            href_locations["player_city"] = clean_pdga_errors(
                clean_string(city))

        combined_data_point.update(href_locations)

    if (player_location):
        combined_data_point["player_location"] = clean_pdga_errors(
            clean_string(player_location))

        if "United States" in player_location:
            combined_data_point["player_country"] = "United States"
            combined_data_point["player_country_short"] = "US"

    return combined_data_point
