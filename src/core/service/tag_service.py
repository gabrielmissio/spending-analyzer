import repository.tag.tag_repository as tag_repository
import repository.register.register_tag_repository as register_tag_repository
from utils.date_time import get_date_now
from model.peewee.base_model import db

def get_tag_by_id(id):
    result = tag_repository.get_by_id(id)
    return result

def get_tags(pagenate_by, current_page):
    page = 0
    result = tag_repository.get_all(page)
    return result

def create_tag(payload):
    with db.transaction() as txn:  
        try:
            payload['updated_at'] = get_date_now()
            payload['inserted_at'] = payload['inserted_at'] if 'inserted_at' in payload else get_date_now()
            tag_id = tag_repository.create(payload)
            txn.commit()
            result = tag_repository.get_by_id(tag_id)
            return result
        except Exception as err:
            print(err)
            txn.rollback()
            raise Exception('Error to register tag')

def update_tag_by_id(id, payload):
    payload['updated_at'] = get_date_now()
    tag_repository.update_by_id(id, payload)
    result = tag_repository.get_by_id(id)
    return result

def delete_register_by_id(id):
    result = tag_repository.delete_by_id(id)
    return result