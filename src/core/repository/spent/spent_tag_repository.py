from model.peewee.spent_tag_model import *

def create(payload):
    spent_model = SpentTagModel(spent_id = payload['spent_id'], tag_id = payload['tag_id'])
    spent_model.save()
    return 0