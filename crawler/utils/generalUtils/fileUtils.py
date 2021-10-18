import json
 

def openJsonFile(filePath: str) -> json:
    """
    Open JSON file and return the content
    """
    f = open(filePath)
    data = json.load(f)
    f.close()

    return data