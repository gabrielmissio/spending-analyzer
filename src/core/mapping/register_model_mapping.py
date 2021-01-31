import json
from datetime import datetime, date

def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()

def mapping_register(db_result, tag_list):
    payload = json.loads(json.dumps(db_result, default=default))
    result_formatted = {
        'id': (payload['id']),
        'description': (payload['description']),
        'value': (payload['value']),
        'inserted_at': (payload['inserted_at']),
        'updated_at': (payload['updated_at']),
        'tags': tag_list
    }

    return result_formatted

def mapping_registers(list_result):
    
    result_formatted = {
        'register': list_result
    }

    return result_formatted