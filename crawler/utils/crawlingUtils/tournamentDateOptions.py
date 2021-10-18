import datetime
from typing import Literal
from utils.generalUtils.errorUtils import raiseError

crawlOptionTypes: str = Literal['all', 'latest', 'test']

def TournamentDate(dateOption: str) -> str:
    tournamentCrawlDates = {
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

    dateOptions = tournamentCrawlDates.get(dateOption)

    if dateOptions:
        startDate = dateOptions.get("startDate")
        endDate = dateOptions.get("endDate")
        url = f'https://www.pdga.com/tour/search?date_filter[min][date]={startDate}&date_filter[max][date]={endDate}'
    else:
        raiseError("INCORRECT_TOURNAMENT_DATE")

    return url