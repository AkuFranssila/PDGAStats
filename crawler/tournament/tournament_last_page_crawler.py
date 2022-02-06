import requests
from bs4 import BeautifulSoup

from utils.generalUtils.errorUtils import raise_error


def tournament_last_page_crawler(link: str) -> int:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    # Check if last page links are found ie. more than 1 page of results
    if (soup.find(class_="pager-last last")):
        last_page = soup.find(
            class_="pager-last last").find('a')['href'].split('page=')[1]
        last_page = int(last_page) + 1
        return last_page
    elif (soup.find(class_="view-footer")):
        last_page = soup.find(
            class_="view-footer").find("p").text.split(' of ')[-1]
        if (last_page.isdigit()):
            return 1
        else:
            raise_error("TOURNAMENT_LAST_PAGE_FAILED_TO_PARSE")
    else:
        raise_error("TOURNAMENT_LAST_PAGE_FAILED_TO_PARSE")
