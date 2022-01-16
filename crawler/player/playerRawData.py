import datetime
import json

class PlayerRawData:
    """
    Creates an object that stores raw data of the crawled player. 

    This data can be saved to S3 or locally.
    """
    def __init__(self, pdga_number: int, raw_data: str, status_code: int) -> None:
        self.pdga_number = pdga_number
        self.crawl_datetime = datetime.datetime.now()
        self.raw_data = raw_data
        self.status_code = status_code
        self.json_data = None

    def create_json(self) -> None:
        json_data = {
            'pdga_number': str(self.pdga_number),
            'crawl_datetime': str(self.crawl_datetime),
            'data': str(self.raw_data),
            'status_code': str(self.status_code)
        }

        self.json_data = json_data

    def print_json(self) -> None:
        print(json.dumps(self.json_data, indent=4))
