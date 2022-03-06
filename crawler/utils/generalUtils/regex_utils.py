import re

TOURNAMENT_URL_REGEX = "\/tour\/event\/(\d){1,6}"
FIRST_MIDDLE_LAST_NAME_REGEX = "(?P<player_first_name>\S+)\s(?:(?P<player_middle_name>\S*)\s)?(?P<player_last_name>\S+)$"
LOCATION_HREF_REGEX = "\/players\?City(?P<player_city>=[^&]*)(?:&StateProv(?P<player_state_short>=[^&]*))?(?:&Country(?P<player_country_short>=[^&]*))?"

# Test href = /players?City=Huntingtn%20Bch&StateProv=CA&Country=FI


def find_first_middle_last_names(player_name) -> dict:
    """
    Finds first, middle and last names from name. Returns dict in following format: {'player_first_name': 'Aku', 'player_middle_name': None, 'player_last_name': 'Franssila'}
    """

    names = re.compile(FIRST_MIDDLE_LAST_NAME_REGEX)
    names = names.match(player_name).groupdict()

    return names


def find_locations_from_href(href) -> dict:
    """
    Finds locations from location href in the data. Returns dict in following format: 
    """

    locations = re.compile(LOCATION_HREF_REGEX)
    locations = locations.match(href).groupdict()

    return locations
