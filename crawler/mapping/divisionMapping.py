divisionMappingOpenPro = {
    "MPO": "Pro Open",
}

divisionMappingOpenProMasters = {
    "MP40": "Pro Master 40+",
    "MP50": "Pro Master 50+",
    "MP60": "Pro Master 60+",
    "MP65": "Pro Master 65+",
    "MP70": "Pro Master 70+",
    "MP75": "Pro Master 75+",
    "MP80": "Pro Master 80+",
}

divisionMappingOpenAmateur = {
    "MA1": "Advanced",
    "MA2": "Intermediate",
    "MA3": "Recreational",
    "MA4": "Novice",
}

divisionMappingOpenAmateurMasters = {
    "MA40": "Amateur Master 40+",
    "MA50": "Amateur Master 50+",
    "MA60": "Amateur Master 60+",
    "MA65": "Amateur Master 65+",
    "MA70": "Amateur Master 70+",
}

divisionMappingOpenJunior = {
    "MJ18": "Junior ≤18",
    "MJ15": "Junior ≤15",
    "MJ12": "Junior ≤12",
    "MJ10": "Junior ≤10",
    "MJ08": "Junior ≤8",
    "MJ06": "Junior ≤6",
}

divisionMappingWomenPro = {
    "FPO": "Pro Open Women"
}

divisionMappingWomenProMasters = {
    "FP40": "Pro Master Women 40+",
    "FP50": "Pro Master Women 50+",
    "FP60": "Pro Master Women 60+",
    "FP65": "Pro Master Women 65+",
    "FP70": "Pro Master Women 70+",
}

divisionMappingWomenAmateur = {
    "FA1": "Advanced Women",
    "FA2": "Intermediate Women",
    "FA3": "Recreational Women",
    "FA4": "Novice Women",
}

divisionMappingWomenAmateurMasters = {
    "FA40": "Amateur Master Women 40+",
    "FA50": "Amateur Master Women 50+",
    "FA60": "Amateur Master Women 60+",
    "FA65": "Amateur Master Women 65+",
    "FA70": "Amateur Master Women 70+",
}

divisionMappingWomenJunior = {
    "FJ18": "Junior Girls ≤18",
    "FJ15": "Junior Girls ≤15",
    "FJ12": "Junior Girls ≤12",
    "FJ10": "Junior Girls ≤10",
    "FJ08": "Junior Girls ≤8",
    "FJ06": "Junior Girls ≤6",
}

divisionMappingRatingsEvents = {
    "RPA": "Gold (Professional division)",
    "RAH": "Blue",
    "RAD": "White",
    "RAE": "Red",
    "RAF": "Green",
    "RAG": "Purple",
}

divisionMappingAllOpen = {**divisionMappingOpenPro, **divisionMappingOpenProMasters, **divisionMappingOpenAmateur, **divisionMappingOpenAmateurMasters, **divisionMappingOpenJunior}
divisionMappingAllWomen = {**divisionMappingWomenPro, **divisionMappingWomenProMasters, **divisionMappingWomenAmateur, **divisionMappingWomenAmateurMasters, **divisionMappingWomenJunior}
divisionMappingAllOpenPro = {**divisionMappingOpenPro, **divisionMappingOpenProMasters}
divisionMappingAllWomenPro = {**divisionMappingWomenPro, **divisionMappingWomenProMasters}
divisionMappingAllOpenAmateur = {**divisionMappingOpenAmateur, **divisionMappingOpenAmateurMasters}
divisionMappingAllOpenMasters = {**divisionMappingOpenProMasters, **divisionMappingOpenAmateurMasters}
divisionMappingAllWomenAmateur = {**divisionMappingWomenAmateur, **divisionMappingWomenAmateurMasters}
divisionMappingAllWomenMasters = {**divisionMappingWomenProMasters, **divisionMappingWomenAmateurMasters}
divisionMappingAllMasters = {**divisionMappingAllOpenMasters, **divisionMappingAllWomenMasters}
divisionMappingAllAmateur = {**divisionMappingAllOpenAmateur, **divisionMappingAllWomenAmateur}
divisionMappingAllJunior = {**divisionMappingOpenJunior, **divisionMappingWomenJunior}
divisionMappingAllAgeRestricted = {**divisionMappingAllMasters, **divisionMappingAllJunior}
divisionMappingAllOpenWomen = {**divisionMappingAllOpen, **divisionMappingAllWomen}
divisionMappingAll = {**divisionMappingAllOpenWomen, **divisionMappingRatingsEvents}

