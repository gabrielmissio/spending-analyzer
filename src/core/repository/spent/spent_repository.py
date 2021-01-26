from model.peewee.spent_model import *
from model.peewee.spent_tag_model import *
from model.peewee.tag_model import *
from mapping import tag_model_mapping as tag_model_mapping
from mapping import spent_model_mapping as spent_model_mapping
from utils.validation import raise_errors
import peewee

def create(payload):
    spent = SpentModel(description = payload['description'], value = payload['value'], inserted_at = payload['inserted_at'], updated_at = payload['updated_at'])
    spent.save()
    return spent.id

def get_by_id(id):
    spent_result = SpentModel.select(SpentModel, TagModel, TagModel.id.alias('tag_id')).join(SpentTagModel, peewee.JOIN.LEFT_OUTER, on=(SpentTagModel.spent_id == SpentModel.id)).join(TagModel, peewee.JOIN.LEFT_OUTER, on=(TagModel.id == SpentTagModel.tag_id)).where(SpentModel.id == id).dicts()
    
    tag_list = []

    for spent in spent_result:
        tag = tag_model_mapping.mapping_tag(spent)
        if tag not in tag_list:
            tag_list.append(tag)

    if spent_result.exists():
        return spent_model_mapping.mapping_spent(spent_result[0], tag_list)

    raise_errors(["Spend not found"])

def get_all(page):
    result = 0
    return result

def update_by_id(id, payload):
    result = 0
    return result

def delete_by_id(id):
    result = 0
    return result    