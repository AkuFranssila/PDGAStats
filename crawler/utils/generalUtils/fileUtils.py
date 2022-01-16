import json
import logging


def open_json_file(file_path: str) -> json:
    """
    Open JSON file and return the content
    """
    f = open(file_path)
    data = json.load(f)
    f.close()

    if data:
        return data
    else:
        print("Unable to open file with path " + file_path)
        return ''
