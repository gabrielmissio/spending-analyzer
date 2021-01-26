from model.peewee.spent_tag_model import *

def create(payload):
    spent_model = SpentTagModel(spent_id = payload['spent_id'], tag_id = payload['tag_id'])
    spent_model.save()
    return 0

def delete_all_by_spent_id(spent_id):
    query = SpentTagModel.delete().where(SpentTagModel.spent_id == spent_id)
    query.execute()
    return 0
