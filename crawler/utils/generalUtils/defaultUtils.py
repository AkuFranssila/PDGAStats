def defaultTo(value: any, returnValue: any) -> any:
    """
    Checks if value exists and if it does returns it unchanged.
    If value does not exists returns a default value.

    str = defaultTo(None, "")
    str -> ""
    """
    if value:
        return value
    else:
        return returnValue