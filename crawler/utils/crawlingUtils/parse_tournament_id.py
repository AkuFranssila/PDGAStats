from utils.generalUtils.errorUtils import raise_error


def parse_tournament_id(tournament_url: str) -> int:
    """
    Parse tournament int from partial or full url.
    """

    parsed_url = ''

    if ("tour/event/" in tournament_url):
        parsed_url = tournament_url.split(
            'tour/event/')[1].split('?')[0].split("&")[0]
        if (parsed_url.isdigit()):
            parsed_url = int(parsed_url)
            return parsed_url
        else:
            print(f'Tournament id was: {parsed_url}')
            raise_error("TOURNAMENT_ID_NOT_INT")
    else:
        raise_error("INVALID_TOURNAMENT_URL")
