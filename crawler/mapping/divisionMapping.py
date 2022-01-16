DIVISION_OPEN_PRO = {
    "MPO": "Pro Open",
}

DIVISION_OPEN_PRO_MASTERS = {
    "MP40": "Pro Master 40+",
    "MP50": "Pro Master 50+",
    "MP60": "Pro Master 60+",
    "MP65": "Pro Master 65+",
    "MP70": "Pro Master 70+",
    "MP75": "Pro Master 75+",
    "MP80": "Pro Master 80+",
}

DIVISION_OPEN_AMATEUR = {
    "MA1": "Advanced",
    "MA2": "Intermediate",
    "MA3": "Recreational",
    "MA4": "Novice",
}

DIVISION_OPEN_AMATEUR_MASTERS = {
    "MA40": "Amateur Master 40+",
    "MA50": "Amateur Master 50+",
    "MA60": "Amateur Master 60+",
    "MA65": "Amateur Master 65+",
    "MA70": "Amateur Master 70+",
}

DIVISION_OPEN_JUNIOR = {
    "MJ18": "Junior ≤18",
    "MJ15": "Junior ≤15",
    "MJ12": "Junior ≤12",
    "MJ10": "Junior ≤10",
    "MJ08": "Junior ≤8",
    "MJ06": "Junior ≤6",
}

DIVISION_WOMEN_PRO = {
    "FPO": "Pro Open Women"
}

DIVISION_WOMEN_PRO_MASTERS = {
    "FP40": "Pro Master Women 40+",
    "FP50": "Pro Master Women 50+",
    "FP60": "Pro Master Women 60+",
    "FP65": "Pro Master Women 65+",
    "FP70": "Pro Master Women 70+",
}

DIVISION_WOMEN_AMATEUR = {
    "FA1": "Advanced Women",
    "FA2": "Intermediate Women",
    "FA3": "Recreational Women",
    "FA4": "Novice Women",
}

DIVISION_WOMEN_AMATEUR_MASTERS = {
    "FA40": "Amateur Master Women 40+",
    "FA50": "Amateur Master Women 50+",
    "FA60": "Amateur Master Women 60+",
    "FA65": "Amateur Master Women 65+",
    "FA70": "Amateur Master Women 70+",
}

DIVISION_WOMEN_JUNIOR = {
    "FJ18": "Junior Girls ≤18",
    "FJ15": "Junior Girls ≤15",
    "FJ12": "Junior Girls ≤12",
    "FJ10": "Junior Girls ≤10",
    "FJ08": "Junior Girls ≤8",
    "FJ06": "Junior Girls ≤6",
}

DIVISION_RATINGS_EVENTS = {
    "RPA": "Gold (Professional division)",
    "RAH": "Blue",
    "RAD": "White",
    "RAE": "Red",
    "RAF": "Green",
    "RAG": "Purple",
}

DIVISION_ALL_OPEN = {**DIVISION_OPEN_PRO, **DIVISION_OPEN_PRO_MASTERS, **DIVISION_OPEN_AMATEUR, **DIVISION_OPEN_AMATEUR_MASTERS, **DIVISION_OPEN_JUNIOR}
DIVISION_ALL_WOMEN = {**DIVISION_WOMEN_PRO, **DIVISION_WOMEN_PRO_MASTERS, **DIVISION_WOMEN_AMATEUR, **DIVISION_WOMEN_AMATEUR_MASTERS, **DIVISION_WOMEN_JUNIOR}
DIVISION_ALL_OPEN_PRO = {**DIVISION_OPEN_PRO, **DIVISION_OPEN_PRO_MASTERS}
DIVISION_ALL_WOMEN_PRO = {**DIVISION_WOMEN_PRO, **DIVISION_WOMEN_PRO_MASTERS}
DIVISION_ALL_OPEN_AMATEUR = {**DIVISION_OPEN_AMATEUR, **DIVISION_OPEN_AMATEUR_MASTERS}
DIVISION_ALL_OPEN_MASTERS = {**DIVISION_OPEN_PRO_MASTERS, **DIVISION_OPEN_AMATEUR_MASTERS}
DIVISION_ALL_WOMEN_AMATEUR = {**DIVISION_WOMEN_AMATEUR, **DIVISION_WOMEN_AMATEUR_MASTERS}
DIVISION_ALL_WOMEN_MASTERS = {**DIVISION_WOMEN_PRO_MASTERS, **DIVISION_WOMEN_AMATEUR_MASTERS}
DIVISION_ALL_MASTERS = {**DIVISION_ALL_OPEN_MASTERS, **DIVISION_ALL_WOMEN_MASTERS}
DIVISION_ALL_AMATEUR = {**DIVISION_ALL_OPEN_AMATEUR, **DIVISION_ALL_WOMEN_AMATEUR}
DIVISION_ALL_JUNIOR = {**DIVISION_OPEN_JUNIOR, **DIVISION_WOMEN_JUNIOR}
DIVISION_ALL_AGE_RESTRICTED = {**DIVISION_ALL_MASTERS, **DIVISION_ALL_JUNIOR}
DIVISION_ALL_OPEN_AND_WOMEN = {**DIVISION_ALL_OPEN, **DIVISION_ALL_WOMEN}
DIVISION_ALL = {**DIVISION_ALL_OPEN_AND_WOMEN, **DIVISION_RATINGS_EVENTS}

