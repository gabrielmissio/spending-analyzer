import peewee
import psycopg2
from playhouse.postgres_ext import *
from datetime import *

db = PostgresqlExtDatabase('postgres', user='postgres', password='666forever',
                           host='spending-analyzer.cdbqu7aguyat.us-east-1.rds.amazonaws.com', port=5432)

class BaseModel(peewee.Model):
    #Modelo Base de PostgreSQL
    class Meta:
        database = db