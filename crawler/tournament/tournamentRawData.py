import datetime
import json


class TournamentRawData:
    """
    Creates an object that stores raw data of the crawled tournament. 

    This data can be saved to S3 or locally.
    """

    def __init__(self, tournament_id: int, raw_data: str, status_code: int) -> None:
        self.tournament_id = tournament_id
        self.crawl_datetime = datetime.datetime.now()
        self.raw_data = raw_data
        self.status_code = status_code
        self.json_data = None

    def create_json(self) -> None:
        created_json = {
            'tournament_id': str(self.tournament_id),
            'crawl_datetime': str(self.crawl_datetime),
            'data': str(self.raw_data),
            'status_code': str(self.status_code)
        }

        self.json_data = created_json

    def print_json(self) -> None:
        print(json.dumps(self.json_data, indent=4))
