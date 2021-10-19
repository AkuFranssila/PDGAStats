import random
import datetime
from crawler.utils.generalUtils.defaultUtils import defaultTo

from mapping.pdgaFieldMapping import pdgaPlayerClassification, membershipStatusMappingAll
from mapping.dateTimeMapping import monthShortToMonthFull, monthShortToMonthNumber
from mapping.stateMapping import statesFullUS
from mapping.divisionMapping import divisionMappingAllOpenWomen
from mapping.eventTierMapping import eventTierMapping

from utils.testUtils.randomCityNames import randomCityNames

randomYearsPlayedType = list[int]

def generateNoneRandomly(input: any) -> any:
    randInt = generateRandomNumberBetween(1, 20)

    if randInt > 5:
        return input
    else:
        return None

def generateRandomNumberBetween(start: int, end: int) -> int:
    randInt = random.randint(start, end)

    return randInt

def generateRandomPdgaNumber() -> int:
    randInt = random.randint(1, 999_999)

    return randInt

def generateRandomTournamentId() -> int:
    randInt = random.randint(1, 99_999)

    return randInt

def generateRandomMoneyAmount() -> float:
    randFloat = round(random.uniform(0.00, 9_999_999.99), 2)

    return randFloat

def generateRandomMemberSince() -> int:
    randInt = random.randint(1960, datetime.datetime.now().year)

    return randInt

def generateRandomRating() -> int:
    randInt = random.randint(1, 1150)

    return randInt

def generateRandomRatingChange() -> int:
    randInt = random.randrange(-150, 150)

    return randInt

def generateRandomEventCount() -> int:
    randInt = random.randint(0, 999)

    return randInt

def generateRandomEventWins() -> int:
    randInt = random.randint(0, 999)

    return randInt

def generateRandomTournamentPosition() -> int:
    """
    Returns random position number between 1 to 999
    """
    randInt = random.randint(1, 999)

    return randInt

def generateRandomPoints() -> float:
    randFloat = round(random.uniform(0.00, 9_999.99), 2)

    return randFloat

def generateRandomCoursePar(holes: int = 18) -> int:
    """
    Generates random course par. Defaults to 18 hole course.

    Minimum par is holes times 3 with random number of additional par up to number of holes.
    """
    randInt = holes * 3 + random.randint(0, holes)

    return randInt

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
    randIntList = random.sample(range(1960, datetime.datetime.now().year), random.randint(0, 30))

    return randIntList

def generateRandomDivision() -> str:
    """
    """
    randDiv = random.choice(
        divisionMappingAllOpenWomen.keys()
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
    randStatus = random.choice(membershipStatusMappingAll)
    
    return randStatus

def generateRandomEventTier() -> str:
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
    randStatus = random.choice([
        eventTierMapping.keys()
        ])
    
    return randStatus

def generateRandomClassification(shortType: bool = False) -> str:
    """
    Returns random PDGA Classification Amateur or Professional.

    Option to return the short version of status AM or PRO
    """

    randInt = random.randint(0, 1)
    if shortType:
        randomClassification = pdgaPlayerClassification.values()[randInt]
    else:
        randomClassification = pdgaPlayerClassification.keys()[randInt]

    return randomClassification

def generateRandomYear() -> int:
    """
    Returns random year between 1960 to current year
    """
    randYear = random.randint(1960, datetime.datetime.now().year)

    return randYear

def generateRandomMonth() -> int:
    """
    Returns random month number 1, 2, 3, 4, 5, 6, 7
    """
    randMonth = random.randint(1, 12)

    return randMonth

def generateRandomMonthShortName() -> str:
    """
    Returns month in format Jan, Feb, Mar...
    """
    randMonth = generateRandomNumberBetween(0, 11)

    randomMonthShortName = monthShortToMonthFull.keys()[randMonth]

    return randomMonthShortName

def generateRandomMonthFullName() -> str:
    """
    Returns month in format January, February...
    """
    randMonth = generateRandomNumberBetween(0, 11)

    randomMonthFullName = monthShortToMonthFull.values()[randMonth]

    return randomMonthFullName

def generateRandomMonthNumberString() -> str:
    """
    Returns month in format 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12
    """
    randMonth = generateRandomNumberBetween(0, 11)

    randomMonthNumberString = monthShortToMonthNumber.values()[randMonth]

    return randomMonthNumberString

def generateRandomDay() -> int:
    randDay = generateRandomNumberBetween(1, 31)

    return randDay

def generateRandomCity() -> str:
    randInt = random.randint(0, len(randomCityNames))

    randomCity = randomCityNames[randInt]

    return randomCity

def generateRandomUSStateFull() -> str:
    usStates = statesFullUS.keys()
    randInt = random.randint(0, len(usStates))
    randomState = usStates[randInt]

    return randomState

def generateRandomUSStateShort() -> str:
    usStates = statesFullUS.values()
    randInt = random.randint(0, len(usStates))
    randomState = usStates[randInt]

    return randomState

def generateRandomUnitedStatesLocation() -> str:
    city = generateNoneRandomly(generateRandomCity())
    if city:
        state = generateRandomUSStateFull()
    else:
        state = generateNoneRandomly(generateRandomUSStateFull())
    
    location = f'{defaultTo(city, "")}, {defaultTo(state, "")}, United States'
    location = location.lstrip(",").strip()

    return location