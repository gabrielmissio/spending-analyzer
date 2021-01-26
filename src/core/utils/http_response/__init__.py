import json
from datetime import datetime, date

def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()

def create_success_body(data):
    result = {}
    result["statusCode"] = 200
    result["headers"] = {}
    result["body"] = json.dumps(data, default=default) if not data is None else None
    return result

def create_error_body(data):
    status_code = 500
    if len(data.args) > 1:
        status_code = data.args[1]
    body = {}
    body["message"] = data.args[0]
    result = {}
    result["statusCode"] = status_code
    result["headers"] = {}
    result["body"] = json.dumps(body)
    
    return result
