from bs4 import BeautifulSoup


def load_data_soup(data: any, parser="html.parser"):
    return BeautifulSoup(data, parser)
