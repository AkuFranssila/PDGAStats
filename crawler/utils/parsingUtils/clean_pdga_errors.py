from mapping.pdga_mapping import PDGA_CITY_MAPPING


def clean_pdga_errors(string: str) -> str:
    for key in PDGA_CITY_MAPPING.keys():
        if key in string:
            string = string.replace(key, PDGA_CITY_MAPPING.get(key))

    return string
