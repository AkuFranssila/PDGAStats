def combine_dictionaries_and_lists(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1 and isinstance(value, list):
            dict1[key].extend(value)
        else:
            dict1[key] = value
