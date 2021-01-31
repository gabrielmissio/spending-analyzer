from model.peewee.register_model import *
from model.peewee.register_tag_model import *
from model.peewee.tag_model import *
from mapping import tag_model_mapping as tag_model_mapping
from mapping import register_model_mapping as register_model_mapping
from utils.validation import raise_errors
import peewee

def create(payload):
    spent = RegisterModel(type = payload['type'], description = payload['description'], value = payload['value'], inserted_at = payload['inserted_at'], updated_at = payload['updated_at'])
    spent.save()
    return spent.id

def get_by_id(id):
    spent_result = RegisterModel.select(RegisterModel, TagModel, TagModel.id.alias('tag_id')).join(RegisterTagModel, peewee.JOIN.LEFT_OUTER, on=(RegisterTagModel.register_id == RegisterModel.id)).join(TagModel, peewee.JOIN.LEFT_OUTER, on=(TagModel.id == RegisterTagModel.tag_id)).where(RegisterModel.id == id).dicts()
    
    tag_list = []

    for spent in spent_result:
        tag = tag_model_mapping.mapping_tag(spent)
        if tag not in tag_list:
            tag_list.append(tag)

    if spent_result.exists():
        return register_model_mapping.mapping_register(spent_result[0], tag_list)

    raise_errors(["Spend not found"])

def get_all(page):
    list_result = []
    spents = RegisterModel.select().order_by(RegisterModel.id)
    for spent in spents:
        print(spent)
        list_result.append(get_by_id(spent))
    print(list_result)
    result = register_model_mapping.mapping_registers(list_result)
    return result

def update_by_id(id, payload):
    query = RegisterModel.update(type = payload['type'], description = payload['description'], value = payload['value'], updated_at = payload['updated_at']).where(RegisterModel.id == id)
    query.execute()  # R
    return 0

def delete_by_id(id):
    result = 0
    return result 
