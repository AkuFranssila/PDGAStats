import logging
import requests

from utils.crawlingUtils.validatePlayerId import validate_player_id

from bs4 import BeautifulSoup

logging.getLogger().setLevel("INFO")


def player_latest_id_crawler() -> int:
    """
    Check the last player on the PDGA players page and collect the PDGA number of the player.
    """
    response = requests.get(
        'https://www.pdga.com/players?FirstName=&LastName=&PDGANum=&Status=All&Class=All&MemberType=All&City=&StateProv=All&Country=All&Country_1=All&UpdateDate=&order=PDGANum&sort=desc')
    soup = BeautifulSoup(response.text, "html.parser")
    latest_player_id = soup.find(
        'td', class_="views-field views-field-PDGANum active pdga-number").text.strip()
    latest_player_id = validate_player_id(latest_player_id)

    return latest_player_id


if __name__ == "__main__":
    player_latest_id = player_latest_id_crawler()
    print(player_latest_id)
