import datetime
from typing import Literal
from utils.generalUtils.errorUtils import raise_error

crawlOptionTypes: str = Literal['all', 'latest', 'test']


def tournament_date(date_option: str) -> str:
    tournament_crawL_dates = {
        "all": {
            "startDate": "1979-01-01",
            "endDate": str(datetime.datetime.today().year) + '-12-31'
        },
        "latest": {
            "startDate": str(datetime.date.today().year) + '-' + str(datetime.date.today().month - 2 if datetime.date.today().month > 1 else 12) + '-' + str(datetime.date.today().day),
            "endDate": str(datetime.datetime.today().year) + '-12-31'
        },
        "test": {
            "startDate": "2019-11-01",
            "endDate": "2019-11-05"
        }
    }

    date_options = tournament_crawL_dates.get(date_option)

    if date_options:
        start_date = date_options.get("startDate")
        end_date = date_options.get("endDate")
        url = f'https://www.pdga.com/tour/search?date_filter[min][date]={start_date}&date_filter[max][date]={end_date}'
    else:
        raise_error("INCORRECT_TOURNAMENT_DATE")

    return url
