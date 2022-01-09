import json
import logging
 

def openJsonFile(filePath: str) -> json:
    """
    Open JSON file and return the content
    """
    f = open(filePath)
    data = json.load(f)
    f.close()
    
    if data:
        return data
    else:
        print("Unable to open file with path " + filePath)
        return ''
