import sys
sys.path.append('/opt')
import json
from model.peewee.spent_model import *

# import requests


def handler(event, context):
   

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "end point get spent by id",
            # "location": ip.text.replace("\n", "")
        }),
    }
