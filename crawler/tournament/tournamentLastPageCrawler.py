import requests
from bs4 import BeautifulSoup

def tournamentLastPage(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    last_page = soup.find(class_="pager-last last").find('a')['href'].split('page=')[1]
    last_page = int(last_page) + 1
    return last_page