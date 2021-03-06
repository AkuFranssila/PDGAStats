import datetime
from dateutil.relativedelta import relativedelta
from typing import Literal
from utils.generalUtils.errorUtils import raise_error

crawlOptionTypes: str = Literal['all', 'latest', 'test']


def tournament_date_options(date_option: str) -> str:
    tournament_crawl_dates = {
        "all": {
            "startDate": "1979-01-01",
            "endDate": datetime.datetime(datetime.datetime.today().year, 12, 31).strftime("%Y-%m-%d")
        },
        "latest": {
            "startDate": (datetime.date.today() - relativedelta(months=+2)).strftime("%Y-%m-%d"),
            "endDate": datetime.datetime(datetime.datetime.today().year, 12, 31).strftime("%Y-%m-%d")
        },
        "test": {
            "startDate": "2021-11-01",
            "endDate": "2021-11-05"
        }
    }

    date_options = tournament_crawl_dates.get(date_option)

    if date_options:
        start_date = date_options.get("startDate")
        end_date = date_options.get("endDate")
        url = f'https://www.pdga.com/tour/search?date_filter[min][date]={start_date}&date_filter[max][date]={end_date}'
    else:
        raise_error("INCORRECT_TOURNAMENT_DATE")

    return url
