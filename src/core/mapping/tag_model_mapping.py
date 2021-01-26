import json
from datetime import datetime, date

def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()

def mapping_tag(db_result):
    payload = json.loads(json.dumps(db_result, default=default))
    result_formatted = {
        "id": (payload['tag_id']),
        "name": (payload['name'])
    }

    return result_formatted