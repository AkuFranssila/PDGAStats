from mapping.errorMapping import error_messages, error_messages_type

def raise_error(message: error_messages_type) -> Exception:
    error_message = error_messages.get(message)

    raise Exception(error_message)
