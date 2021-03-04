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
        return tag_model_mapping.mapping_tag(tag_result[0])#'formata e manda'register_model_mapping.mapping_register(register_result[0], tag_list)

    raise_errors(["Spend not found"])

def get_all(pagination):
    tags = TagModel.select().order_by(TagModel.id).paginate(pagination.get_current_page(), pagination.get_paginate_by())
    list_results = []

    pagination.set_all_rows(count_tag())

    for tag in tags:
        list_results.append(get_by_id(tag))

    result = tag_model_mapping.mapping_tags(list_results, pagination)
    return result

def update_by_id(id, payload):
    query = TagModel.update(name = payload['name'], updated_at = payload['updated_at']).where(TagModel.id == id)
    query.execute()
    return 0

def delete_by_id(id):
    result = 0
    return result 

def count_tag():#to-do: to implement filter
    total_tags = TagModel.select().order_by(TagModel.id).count()
    return  total_tags