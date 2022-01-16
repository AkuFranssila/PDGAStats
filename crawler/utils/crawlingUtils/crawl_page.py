import requests
import argparse
import json


def handle_arguments() -> str:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        '--url',
        type=str,
        required=True,
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
    crawl_random_page(url)
