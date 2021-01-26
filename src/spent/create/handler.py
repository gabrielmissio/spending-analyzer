import sys
sys.path.append('/opt')
import json
import service.spent_service as spent_service
from utils.http_response import create_success_body, create_error_body
from utils.validation import spent_validation as spent_validation


# import requests

def handler(event, context):
    try:
        payload = json.loads(event['body'])
        print(payload)

        spent_validation.validate(payload)

        result = spent_service.create_spent(payload)
        print(result)
        return create_success_body(result)
    except Exception as err:
        print(err)
        return create_error_body(err)
