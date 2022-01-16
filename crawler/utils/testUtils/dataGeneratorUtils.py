import random
import datetime
from crawler.utils.generalUtils.defaultUtils import default_to

from mapping.pdgaFieldMapping import PDGA_PLAYER_CLASSIFICATION, MEMBERSHIP_STATUS_ALL
from mapping.dateTimeMapping import MONTH_SHORT_NAME_TO_FULL_NAME, MONTH_SHORT_NAME_TO_NUMBER
from mapping.stateMapping import US_STATES_DICT
from mapping.divisionMapping import DIVISION_ALL_OPEN_AND_WOMEN
from mapping.eventTierMapping import EVENT_TIER_MAPPING

from utils.testUtils.randomCityNames import RANDOM_CITY_NAMES

randomYearsPlayedType = list[int]


def generate_none_randomly(input: any) -> any:
    rand_int = generate_random_number_between(1, 20)

    if rand_int > 5:
        return input
    else:
        return None


def generate_random_number_between(start: int, end: int) -> int:
    random_int = random.random_int(start, end)

    return random_int


def generateRandomPdgaNumber() -> int:
    random_int = random.random_int(1, 999_999)

    return random_int


def generateRandomTournamentId() -> int:
    random_int = random.random_int(1, 99_999)

    return random_int


def generateRandomMoneyAmount() -> float:
    randFloat = round(random.uniform(0.00, 9_999_999.99), 2)

    return randFloat


def generateRandomMemberSince() -> int:
    random_int = random.random_int(1960, datetime.datetime.now().year)

    return random_int


def generateRandomRating() -> int:
    random_int = random.random_int(1, 1150)

    return random_int


def generateRandomRatingChange() -> int:
    random_int = random.randrange(-150, 150)

    return random_int


def generateRandomEventCount() -> int:
    random_int = random.random_int(0, 999)

    return random_int


def generateRandomEventWins() -> int:
    random_int = random.random_int(0, 999)

    return random_int


def generateRandomTournamentPosition() -> int:
    """
    Returns random position number between 1 to 999
    """
    random_int = random.random_int(1, 999)

    return random_int


def generateRandomPoints() -> float:
    randFloat = round(random.uniform(0.00, 9_999.99), 2)

    return randFloat


def generateRandomCoursePar(holes: int = 18) -> int:
    """
    Generates random course par. Defaults to 18 hole course.

    Minimum par is holes times 3 with random number of additional par up to number of holes.
    """
    random_int = holes * 3 + random.random_int(0, holes)

    return random_int


def generateRandomCourseResult(holes: int = 18, par: int = 54) -> int:
    """
    Generate random result for the course based on holes and par.
    Defaults to 18 holes and par 54.

    Returns result that varies between birdie every hole and triple bogey per hole.
    """
    courseResult = par + random.randrange(-1*holes, 3*holes)

    return courseResult


def generateRandomYearsPlayed() -> randomYearsPlayedType:
    """
    Generate random number of years played. Years between 1960 to current year. Years played 0 to 30.

    Returns list of years as int.
    """
    random_intList = random.sample(
        range(1960, datetime.datetime.now().year), random.random_int(0, 30))

    return random_intList


def generateRandomDivision() -> str:
    """
    """
    randDiv = random.choice(
        DIVISION_ALL_OPEN_AND_WOMEN.keys()
    )

    return randDiv


def generateRandomOfficialStatus() -> bool:
    """
    Return True or False for official certified status.

    Player is certified or he isn't.
    """

    randBool = random.choice([True, False])

    return randBool


def generateRandomMembershipStatus() -> str:
    randStatus = random.choice(MEMBERSHIP_STATUS_ALL)

    return randStatus


def generate_random_event_tier() -> str:
    """
    Returns random event tier string

    M - Major
    NT - National Tour
    A - A-tier
    B - B-tier
    C - C-tier
    XM - Experimental Major
    XA - Experimental A-tier
    XB - Experimental B-tier
    XC - Experimental C-tier
    L - League
    H - Historical event
    S - Series
    A/B - Mix of A/B tier
    B/C - Mix of B/C tier
    """
    random_tier = random.choice([
        EVENT_TIER_MAPPING.keys()
    ])

    return random_tier


def generate_random_classification(short_type: bool = False) -> str:
    """
    Returns random PDGA Classification Amateur or Professional.

    Option to return the short version of status AM or PRO
    """

    random_int = random.random_int(0, 1)
    if short_type:
        random_classification = PDGA_PLAYER_CLASSIFICATION.values()[random_int]
    else:
        random_classification = PDGA_PLAYER_CLASSIFICATION.keys()[random_int]

    return random_classification


def generate_random_year() -> int:
    """
    Returns random year between 1960 to current year
    """
    random_year = random.random_int(1960, datetime.datetime.now().year)

    return random_year


def generate_random_month() -> int:
    """
    Returns random month number 1, 2, 3, 4, 5, 6, 7
    """
    random_month = random.random_int(1, 12)

    return random_month


def generate_random_month_with_short_name() -> str:
    """
    Returns month in format Jan, Feb, Mar...
    """
    random_month = generate_random_number_between(0, 11)

    random_month_short_name = MONTH_SHORT_NAME_TO_FULL_NAME.keys()[
        random_month]

    return random_month_short_name


def generate_random_month_with_full_name() -> str:
    """
    Returns month in format January, February...
    """
    random_month = generate_random_number_between(0, 11)

    randomMonthFullName = MONTH_SHORT_NAME_TO_FULL_NAME.values()[random_month]

    return randomMonthFullName


def generate_random_month_number_string() -> str:
    """
    Returns month in format 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12
    """
    random_month = generate_random_number_between(0, 11)

    random_month_number_string = MONTH_SHORT_NAME_TO_NUMBER.values()[
        random_month]

    return random_month_number_string


def generate_random_day() -> int:
    random_day = generate_random_number_between(1, 31)

    return random_day


def generate_random_city() -> str:
    random_int = random.random_int(0, len(RANDOM_CITY_NAMES))

    random_city = RANDOM_CITY_NAMES[random_int]

    return random_city


def generate_random_us_state_with_full_name() -> str:
    us_states = US_STATES_DICT.keys()
    random_int = random.random_int(0, len(us_states))
    random_state = us_states[random_int]

    return random_state


def generate_random_us_state_with_short_name() -> str:
    us_states = US_STATES_DICT.values()
    random_int = random.random_int(0, len(us_states))
    random_state = us_states[random_int]

    return random_state


def generate_random_united_states_location() -> str:
    city = generate_none_randomly(generate_random_city())
    if city:
        state = generate_random_us_state_with_full_name()
    else:
        state = generate_none_randomly(
            generate_random_us_state_with_full_name())

    location = f'{default_to(city, "")}, {default_to(state, "")}, United States'
    location = location.lstrip(",").strip()

    return location
