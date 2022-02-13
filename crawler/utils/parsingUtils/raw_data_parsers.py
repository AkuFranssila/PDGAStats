import json

from utils.generalUtils.defaultUtils import default_to
from utils.parsingUtils.soup_utils import load_data_soup
from utils.parsingUtils.add_failed_data_point import add_failed_data_point
from utils.crawlingUtils.parse_tournament_id import parse_tournament_id


def raw_data_parse_player_name(raw_data) -> json:
    parsed_data_point = {"player_name": None}
    data = load_data_soup(raw_data)

    if (data.find(id="page-title")):
        parsed_data_point["player_name"] = data.find(id="page-title").text
    else:
        add_failed_data_point(parsed_data_point, "player_name")

    return parsed_data_point


def raw_data_parse_player_location(raw_data) -> json:
    parsed_data_point = {"player_location": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="location")):
        parsed_data_point["player_location"] = data.find(
            class_="location").find('a').text
    else:
        add_failed_data_point(parsed_data_point, "player_location")

    return parsed_data_point


def raw_data_parse_player_location_href(raw_data) -> json:
    parsed_data_point = {"player_location_href": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="location")):
        parsed_data_point["player_location_href"] = data.find(
            class_="location").find('a')["href"]
    else:
        add_failed_data_point(parsed_data_point, "player_location_href")

    return parsed_data_point


def raw_data_parse_player_classification(raw_data) -> json:
    parsed_data_point = {"player_classification": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="classification")):
        parsed_data_point["player_classification"] = data.find(
            class_="classification").text
    else:
        add_failed_data_point(parsed_data_point, "player_classification")

    return parsed_data_point


def raw_data_parse_player_member_since(raw_data) -> json:
    parsed_data_point = {"player_member_since": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="join-date")):
        parsed_data_point["player_member_since"] = data.find(
            class_="join-date").text
    else:
        add_failed_data_point(parsed_data_point, "player_member_since")

    return parsed_data_point


def raw_data_parse_player_membership_status(raw_data) -> json:
    parsed_data_point = {"player_membership_status": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="membership-status")):
        parsed_data_point["player_membership_status"] = data.find(
            class_="membership-status").find("a").text
    else:
        add_failed_data_point(parsed_data_point, "player_membership_status")

    return parsed_data_point


def raw_data_parse_player_membership_status_expiration_date(raw_data) -> json:
    parsed_data_point = {"player_membership_status_expiration_date": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="membership-expiration-date")):
        parsed_data_point["player_membership_status_expiration_date"] = data.find(
            class_="membership-expiration-date").text
    else:
        add_failed_data_point(
            parsed_data_point, "player_membership_status_expiration_date")

    return parsed_data_point


def raw_data_parse_player_official_status(raw_data) -> json:
    parsed_data_point = {"player_official_status": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="official")):
        parsed_data_point["player_official_status"] = data.find(
            class_="official").find("a").text
    else:
        add_failed_data_point(parsed_data_point, "player_official_status")

    return parsed_data_point


def raw_data_parse_player_official_status_expiration_date(raw_data) -> json:
    parsed_data_point = {"player_official_status_expiration_date": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="official-expiration-date")):
        parsed_data_point["player_official_status_expiration_date"] = data.find(
            class_="official-expiration-date").text
    else:
        add_failed_data_point(
            parsed_data_point, "player_official_status_expiration_date")

    return parsed_data_point


def raw_data_parse_player_current_rating(raw_data) -> json:
    parsed_data_point = {"player_current_rating": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="current-rating")):
        parsed_data_point["player_current_rating"] = data.find(
            class_="current-rating").text
    else:
        add_failed_data_point(parsed_data_point, "player_current_rating")

    return parsed_data_point


def raw_data_parse_player_current_rating_date(raw_data) -> json:
    parsed_data_point = {"player_current_rating_date": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="rating-date")):
        parsed_data_point["player_current_rating_date"] = data.find(
            class_="rating-date").text
    else:
        add_failed_data_point(parsed_data_point, "player_current_rating_date")

    return parsed_data_point


def raw_data_parse_player_career_events_singles(raw_data) -> json:
    parsed_data_point = {"player_career_events_singles": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="career-events disclaimer")):
        parsed_data_point["player_career_events_singles"] = data.find(
            class_="career-events disclaimer").text
    else:
        add_failed_data_point(
            parsed_data_point, "player_career_events_singles")

    return parsed_data_point


def raw_data_parse_player_singles_wins(raw_data) -> json:
    parsed_data_point = {"player_singles_wins": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="career-wins disclaimer")):
        parsed_data_point["player_singles_wins"] = data.find(
            class_="career-wins disclaimer").find("a").text
    else:
        add_failed_data_point(parsed_data_point, "player_singles_wins")

    return parsed_data_point


def raw_data_parse_player_career_earnings(raw_data) -> json:
    parsed_data_point = {"player_career_earnings": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="career-earnings")):
        parsed_data_point["player_career_earnings"] = data.find(
            class_="career-earnings").text
    else:
        add_failed_data_point(parsed_data_point, "player_career_earnings")

    return parsed_data_point


def raw_data_parse_player_upcoming_events(raw_data) -> json:
    parsed_data_point = {"player_upcoming_events": []}
    data = load_data_soup(raw_data)

    if (data.find(class_="upcoming-events")):
        all_events = data.find(
            class_="upcoming-events").find("ul").find_all("a", href=True)

        for event in all_events:
            event_url = parse_tournament_id(event["href"])
            parsed_data_point["player_upcoming_events"].append(event_url)
    else:
        add_failed_data_point(parsed_data_point, "player_upcoming_events")

    return parsed_data_point


def raw_data_parse_player_years_played(raw_data) -> json:
    parsed_data_point = {"player_years_played": []}
    data = load_data_soup(raw_data)

    if (data.find(class_="year-link")):
        all_years = data.find(
            class_="year-link").find("ul").find_all("a", href=True)

        for year in all_years:
            parsed_data_point["player_years_played"].append(year.text)
    else:
        add_failed_data_point(parsed_data_point, "player_years_played")

    return parsed_data_point


def raw_data_parse_player_picture_url(raw_data) -> json:
    parsed_data_point = {"player_picture_url": None}
    data = load_data_soup(raw_data)

    if (data.find(class_="views-field views-field-colorbox")):
        parsed_data_point["player_picture_url"] = data.find(
            class_="views-field views-field-colorbox").find("img")["src"]
    else:
        add_failed_data_point(parsed_data_point, "player_picture_url")

    return parsed_data_point
