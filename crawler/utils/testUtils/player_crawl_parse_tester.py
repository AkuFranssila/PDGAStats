import json
from player.player_combined_data import PlayerCombinedData

from player.playerRawDataCrawler import player_raw_data_crawler
from player.player_parsed_data import PlayerParsedData


def player_crawl_parse_tester(pdga_number):

    player_raw_data = player_raw_data_crawler(pdga_number)
    player_parsed_data = PlayerParsedData(player_raw_data.json_data)
    player_parsed_data.create_json()
    player_parsed_data.parse_raw_data()

    data = player_parsed_data.parsed_data

    combined_data = PlayerCombinedData(data)
    combined_data.create_json()
    combined_data.combine_data()

    data = combined_data.combined_data

    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    # player_crawl_parse_tester(44708) #Aku
    # player_crawl_parse_tester(38008)
    # player_crawl_parse_tester(8003) #Only country, not US
    # player_crawl_parse_tester(8992)
    # player_crawl_parse_tester(27523) #Mcbeth
    player_crawl_parse_tester(112)  # Only US location
    # player_crawl_parse_tester(80004)  # No location
