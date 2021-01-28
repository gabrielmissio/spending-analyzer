from model.peewee.base_model import BaseModel
import peewee

class TagModel(BaseModel):

    class Meta:
        db_table = 'tag'

    id = peewee.BigIntegerField(null=False, unique=True, primary_key=True)
    inserted_at = peewee.DateTimeField(formats=['%Y-%m-%d %H:%M:%S.%f'])
    updated_at = peewee.DateTimeField(formats=['%Y-%m-%d %H:%M:%S.%f'])
    name = peewee.CharField(null=False)
