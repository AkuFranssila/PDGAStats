import random
import datetime
from crawler.utils.generalUtils.defaultUtils import defaultTo

from mapping.pdgaFieldMapping import pdgaPlayerClassification
from mapping.dateTimeMapping import monthShortToMonthFull, monthShortToMonthNumber
from mapping.stateMapping import statesFullUS

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
    randInt = random.randint(1, 999)

    return randInt

def generateRandomPoints() -> float:
    randFloat = round(random.uniform(0.00, 9_999.99), 2)

    return randFloat

def generateRandomYearsPlayed() -> randomYearsPlayedType:
    randIntList = random.sample(range(1960, datetime.datetime.now().year), random.randint(0, 30))

    return randIntList

def generateRandomOfficialStatus() -> bool:
    randBool = random.choice([True, False])
    
    return randBool

def generateRandomMembershipStatus() -> str:
    randStatus = random.choice([
        "Eagle Club", 
        "Birdie Club", 
        "Ace Club", 
        "Current", 
        "Expired"
        ])
    
    return randStatus

def generateRandomEventTier() -> str:
    randStatus = random.choice([
        "M",
        "NT",
        "A",
        "B",
        "C",
        "XM",
        "XA",
        "XB",
        "XC",
        "L",
        "H",
        "S",
        "A/B",
        "B/C"
        ])
    
    return randStatus

def generateRandomClassification(shortType: bool = False) -> str:
    randInt = random.randint(0, 1)
    if shortType:
        randomClassification = pdgaPlayerClassification.values()[randInt]
    else:
        randomClassification = pdgaPlayerClassification.keys()[randInt]

    return randomClassification

def generateRandomYear() -> int:
    randYear = random.randint(1960, datetime.datetime.now().year)

    return randYear

def generateRandomMonth() -> int:
    randMonth = random.randint(1, 12)

    return randMonth

def generateRandomMonthShortName() -> str:
    randMonth = generateRandomNumberBetween(0, 11)

    randomMonthShortName = monthShortToMonthFull.keys()[randMonth]

    return randomMonthShortName

def generateRandomMonthFullName() -> str:
    randMonth = generateRandomNumberBetween(0, 11)

    randomMonthFullName = monthShortToMonthFull.values()[randMonth]

    return randomMonthFullName

def generateRandomMonthShortName() -> str:
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