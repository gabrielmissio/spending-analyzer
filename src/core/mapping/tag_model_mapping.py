import json
from datetime import datetime, date

def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()

def mapping_tag(db_result):
    payload = json.loads(json.dumps(db_result, default=default))
    result_formatted = {
        "id": (payload['tag_id']),
        "name": (payload['name']),
        "updated_at": (payload['updated_at']),
        "inserted_at": (payload['inserted_at'])
    }

    return result_formatted

def mapping_tags(list_result):
    result_formatted = {
        "tags": list_result
    }

    return result_formatted