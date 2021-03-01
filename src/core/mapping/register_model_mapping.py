import json
from datetime import datetime, date

def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()

def mapping_register(db_result, tag_list):
    payload = json.loads(json.dumps(db_result, default=default))
    result_formatted = {
        'id': (payload['id']),
        'type': (payload['type']),
        'description': (payload['description']),
        'value': (payload['value']),
        'inserted_at': (payload['inserted_at']),
        'updated_at': (payload['updated_at']),
        'tags': tag_list
    }

    return result_formatted

def mapping_registers(list_result, page):
    
    result_formatted = {
        'registers': list_result,
        'metadata': {
            'current_page': page.get_current_page(),
            'total_pages': page.get_page_count(),
            'total_rows()': page.get_all_rows(),
            'next_page': page.get_next_page(),
            'previous_page': page.get_previous_page()
        }
    }

    return result_formatted