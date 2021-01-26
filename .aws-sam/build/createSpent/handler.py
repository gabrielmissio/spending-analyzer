import sys
sys.path.append('/opt')
import json
from model.peewee.spent_model import *

# import requests


def handler(event, context):
    
    teste = SpentModel(description= "teste", value = 5.22)
    teste.save()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "end point create spent",
            # "location": ip.text.replace("\n", "")
        }),
    }
