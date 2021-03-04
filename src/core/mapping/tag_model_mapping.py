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

def mapping_tags(list_result, page):
    result_formatted = {
        "tags": list_result,
        'metadata': {
            'current_page': page.get_current_page(),
            'total_pages': page.get_page_count(),
            'total_rows': page.get_all_rows(),
            'next_page': page.get_next_page(),
            'previous_page': page.get_previous_page()
        }
    }

    return result_formatted