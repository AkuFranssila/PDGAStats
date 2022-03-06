import re


def clean_string(string: str) -> str:
    """
    Takes string and returns it cleaned with most common ways.

    - Remove double whitespace
    - Strip start and end of string of whitespace
    - Remove html space %20

    """

    string = string.strip()
    string = string.replace('%20', ' ')
    string = re.sub(' {2,}', ' ', string)
    string = string.title()

    return string
