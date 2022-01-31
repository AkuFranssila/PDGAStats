import requests
import argparse
import json


def handle_arguments() -> str:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        '--url',
        type=str,
        help="Random page that needs to be crawled. Returns raw content"
    )
    url: str = argument_parser.parse_args().url

    return url


def crawl_random_page(url: str):
    response = requests.get(url)
    data = {
        "content": response.text
    }

    print(json.dumps(data))


if __name__ == "__main__":
    url = handle_arguments()
    url = "https://www.pdga.com/tour/search?date_filter[min][date]=2021-11-01&date_filter[max][date]=2021-11-05"
    crawl_random_page(url)
