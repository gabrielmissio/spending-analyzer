from model.peewee.register_model import *
from model.peewee.register_tag_model import *
from model.peewee.tag_model import *
from mapping import tag_model_mapping as tag_model_mapping
from mapping import register_model_mapping as register_model_mapping
from utils.validation import raise_errors
import peewee

def create(payload):
    tag = TagModel(name = payload['name'], inserted_at = payload['inserted_at'], updated_at = payload['updated_at'])
    tag.save()
    return tag.id

def get_by_id(id):
    tag_result = TagModel.select(TagModel.id.alias('tag_id'),TagModel).where(TagModel.id == id).dicts()

    if tag_result.exists():
        return tag_model_mapping.mapping_tag(tag_result[0])#'formata e manda'register_model_mapping.mapping_register(spent_result[0], tag_list)

    raise_errors(["Spend not found"])

def get_all(page):
    tags = TagModel.select().order_by(TagModel.id)
    list_results = []
    for tag in tags:
        list_results.append(get_by_id(tag))

    result = tag_model_mapping.mapping_tags(list_results)
    return result

def update_by_id(id, payload):
    query = TagModel.update(name = payload['name'], updated_at = payload['updated_at']).where(TagModel.id == id)
    query.execute()  # R
    return 0

def delete_by_id(id):
    result = 0
    return result 
