import repository.register.register_repository as register_repository
import repository.register.register_tag_repository as register_tag_repository
from utils.date_time import get_date_now
from model.peewee.base_model import db

def get_register_by_id(id):
    result = register_repository.get_by_id(id)
    return result

def get_registers(pagenate_by, current_page):
    page = 0
    result = register_repository.get_all(page)
    return result

def create_register(payload):
    with db.transaction() as txn:  
        try:
            payload['updated_at'] = get_date_now()
            payload['inserted_at'] = payload['inserted_at'] if 'inserted_at' in payload else get_date_now()
            register_id = register_repository.create(payload)
            for tag in payload['tags']:
                payload_register_tag = {}
                payload_register_tag['tag_id'] = tag['tag']
                payload_register_tag['register_id'] = register_id
                register_tag_repository.create(payload_register_tag)
            txn.commit()
            result = register_repository.get_by_id(register_id)
            return result
        except Exception as err:
            print(err)
            txn.rollback()
            raise Exception('Error to register register')

def update_register_by_id(id, payload):
    register_tag_repository.delete_all_by_register_id(id)
    for tag in payload['tags']:
        payload_register_tag = {}
        payload_register_tag['tag_id'] = tag['tag']
        payload_register_tag['register_id'] = id
        register_tag_repository.create(payload_register_tag)
    payload['updated_at'] = get_date_now()
    register_repository.update_by_id(id, payload)
    result = register_repository.get_by_id(id)
    return result

def delete_register_by_id(id):
    result = register_repository.delete_by_id(id)
    return result