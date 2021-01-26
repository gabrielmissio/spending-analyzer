from model.peewee.base_model import BaseModel
import peewee

class SpentTagModel(BaseModel):

    class Meta:
        db_table = 'spent_tag'
        primary_key = False

    spent_id = peewee.BigIntegerField(null=False)
    tag_id = peewee.BigIntegerField(null=False)
   
