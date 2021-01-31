import sys
sys.path.append('/opt')
import json
import service.tag_service as tag_service
from utils.http_response import create_success_body, create_error_body


# import requests

def handler(event, context):
    try:
        payload = json.loads(event['body'])
        print(payload)

        #register_validation.validate(payload)

        result = tag_service.create_tag(payload)
        print(result)
        return create_success_body(result)
    except Exception as err:
        print(err)
        return create_error_body(err)
