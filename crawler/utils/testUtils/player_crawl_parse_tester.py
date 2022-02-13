import json

from player.playerRawDataCrawler import player_raw_data_crawler
from player.player_parsed_data import PlayerParsedData


def player_crawl_parse_tester(pdga_number):

    player_raw_data = player_raw_data_crawler(pdga_number)
    player_parsed_data = PlayerParsedData(player_raw_data.json_data)
    player_parsed_data.create_json()
    player_parsed_data.parse_raw_data()

    data = player_parsed_data.parsed_data

    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    # player_crawl_parse_tester(44708)
    # player_crawl_parse_tester(38008)
    # player_crawl_parse_tester(8003)
    player_crawl_parse_tester(8992)
