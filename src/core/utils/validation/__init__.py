def validate_field_error(payload, attr, message):
    if not attr in payload or payload[attr] is None:
        return message

    return None

def raise_errors(errors):
    result = []
    for e in errors:
        if not e is None:
            result.append(e)

    if len(result) > 0:
        message = {}
        message["errors"] = result
        raise Exception(message, 400)