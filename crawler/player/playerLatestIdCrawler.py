import logging
import requests

from utils.crawlingUtils.validatePlayerId import validatePlayerId

from bs4 import BeautifulSoup

logging.getLogger().setLevel("INFO")

def playerLatestIdCrawler() -> int:
    """
    Check the last player on the PDGA players page and collect the PDGA number of the player.
    """
    response = requests.get('https://www.pdga.com/players?FirstName=&LastName=&PDGANum=&Status=All&Class=All&MemberType=All&City=&StateProv=All&Country=All&Country_1=All&UpdateDate=&order=PDGANum&sort=desc')
    soup = BeautifulSoup(response.content, "html.parser")
    latestPlayerId = soup.find(class_="odd views-row-first").find_all('td')[1].text.strip()
    latestPlayerId = validatePlayerId(latestPlayerId)

    return latestPlayerId
    

if __name__ == "__main__":
    playerLatestId = playerLatestIdCrawler()
    print(playerLatestId)