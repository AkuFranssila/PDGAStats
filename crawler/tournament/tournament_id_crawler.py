import requests
from bs4 import BeautifulSoup
import re
from utils.crawlingUtils.parse_tournament_id import parse_tournament_id
from tournament.tournament_last_page_crawler import tournament_last_page_crawler

from utils.generalUtils.regex_utils import TOURNAMENT_URL_REGEX


def tournament_id_crawler(url: str) -> list:
    # Found urls
    parsed_urls = []

    last_page_number = tournament_last_page_crawler(url)

    for page_number in range(0, last_page_number):
        page_url = f'{url}&page={page_number}'

        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Tournament container
        container = soup.find(class_="table-container")
        # Matching urls with regex
        tournament_url_elements = container.find_all(
            "a", {"href": re.compile(TOURNAMENT_URL_REGEX)})

        for element in tournament_url_elements:
            parsed_id = parse_tournament_id(element["href"])
            parsed_urls.append(parsed_id)

    parsed_urls.sort
    parsed_urls_no_duplicates = list(dict.fromkeys(parsed_urls))

    print(f'Found {len(parsed_urls_no_duplicates)} tournaments.')

    return parsed_urls_no_duplicates
