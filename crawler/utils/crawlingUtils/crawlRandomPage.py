import requests
import argparse
import json

def handleArguments() -> str:
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument(
        '--url',
        type=str,
        required=True,
        help="Random page that needs to be crawled. Returns raw content"
        )
    url: str =  argumentParser.parse_args().url

    return url

def crawlRandomPage(url: str):
    response = requests.get(url)
    data = {
        "content": response.text
    }

    print(json.dumps(data))

if __name__ == "__main__":
    url = handleArguments()
    crawlRandomPage(url)