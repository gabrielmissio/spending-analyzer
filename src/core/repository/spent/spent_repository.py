from model.peewee.spent_model import *

def create(payload):
    spent = SpentModel(description = payload['description'], value = payload['value'], inserted_at = payload['inserted_at'], updated_at = payload['updated_at'])
    spent.save()
    return spent.id

def get_by_id(id):
    result = 0
    return result

def get_all(page):
    result = 0
    return result

def update_by_id(id, payload):
    result = 0
    return result

def delete_by_id(id):
    result = 0
    return result    