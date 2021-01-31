from utils.validation import validate_field_error, raise_errors

def validate(payload):
    errors = []
    errors.append(validate_field_error(payload, "description", "description required"))
    errors.append(validate_field_error(payload, "value", "value required"))

    raise_errors(errors)