import repository.spent.spent_repository as spent_repository
import repository.spent.spent_tag_repository as spent_tag_repository
from utils.date_time import get_date_now

def get_spent_by_id(id):
    result = spent_repository.get_by_id(id)
    return result

def get_spents(pagenate_by, current_page):
    page = 0
    result = spent_repository.get_all(page)
    return result

def create_spent(payload):
    payload['updated_at'] = get_date_now()
    payload['inserted_at'] = payload['inserted_at'] if 'inserted_at' in payload else get_date_now()
    #to-do: insert tags on spent_tag table, return get_spends_by_id
    spent_id = spent_repository.create(payload)
    for tag in payload['tags']:
        payload_spent_tag = {}
        payload_spent_tag['tag_id'] = tag['tag']
        payload_spent_tag['spent_id'] = spent_id
        spent_tag_repository.create(payload_spent_tag)
    result = 0
    return result

def update_spent_by_id(id, payload):
    result = spent_repository.update_by_id(id, payload)
    return result

def delete_spent_by_id(id):
    result = spent_repository.delete_by_id(id)
    return result