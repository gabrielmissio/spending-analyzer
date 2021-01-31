from model.peewee.register_tag_model import *

def create(payload):
    register_model = RegisterTagModel(register_id = payload['register_id'], tag_id = payload['tag_id'])
    register_model.save()
    return 0

def delete_all_by_register_id(register_id):
    query = RegisterTagModel.delete().where(RegisterTagModel.register_id == register_id)
    query.execute()
    return 0
