from model.peewee.register_model import *
from model.peewee.register_tag_model import *
from model.peewee.tag_model import *
from mapping import tag_model_mapping as tag_model_mapping
from mapping import register_model_mapping as register_model_mapping
from utils.validation import raise_errors
import peewee

def create(payload):
    register = RegisterModel(type = payload['type'], description = payload['description'], value = payload['value'], inserted_at = payload['inserted_at'], updated_at = payload['updated_at'])
    register.save()
    return register.id

def get_by_id(id):
    register_result = RegisterModel.select(RegisterModel, TagModel, TagModel.id.alias('tag_id')).join(RegisterTagModel, peewee.JOIN.LEFT_OUTER, on=(RegisterTagModel.register_id == RegisterModel.id)).join(TagModel, peewee.JOIN.LEFT_OUTER, on=(TagModel.id == RegisterTagModel.tag_id)).where(RegisterModel.id == id).dicts()
    
    tag_list = []

    for register in register_result:
        tag = tag_model_mapping.mapping_tag(register)
        if tag not in tag_list:
            tag_list.append(tag)

    if register_result.exists():
        return register_model_mapping.mapping_register(register_result[0], tag_list)

    raise_errors(["Spend not found"])

def get_all(page):
    list_result = []
    registers = RegisterModel.select().order_by(RegisterModel.id)
    for register in registers:
        print(register)
        list_result.append(get_by_id(register))
    print(list_result)
    result = register_model_mapping.mapping_registers(list_result)
    return result

def update_by_id(id, payload):
    query = RegisterModel.update(type = payload['type'], description = payload['description'], value = payload['value'], updated_at = payload['updated_at']).where(RegisterModel.id == id)
    query.execute()  # 
    return 0

def delete_by_id(id):
    result = 0
    return result 
