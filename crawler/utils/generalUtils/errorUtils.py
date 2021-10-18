from mapping.errorMapping import errorMessages, errorMessagesType

def raiseError(message: errorMessagesType) -> Exception:
    errorMessage = errorMessages.get(message)

    raise Exception(errorMessage)
