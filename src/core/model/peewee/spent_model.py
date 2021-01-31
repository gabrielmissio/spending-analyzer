from model.peewee.base_model import BaseModel
import peewee

class SpentModel(BaseModel):

    class Meta:
        db_table = 'register'

    id = peewee.BigIntegerField(null=False, unique=True, primary_key=True)
    inserted_at = peewee.DateTimeField(formats=['%Y-%m-%d %H:%M:%S.%f'])
    updated_at = peewee.DateTimeField(formats=['%Y-%m-%d %H:%M:%S.%f'])
    description = peewee.CharField(null=False)
    type = peewee.CharField(null=False)
    value = peewee.DoubleField(null=False)
