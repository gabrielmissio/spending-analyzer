import sys
sys.path.append('/opt')
import json
import service.register_service as register_service
from utils.http_response import create_success_body, create_error_body

def handler(event, context):
    try:
        print(event)
        id = event['pathParameters']['id']

        result = register_service.get_register_by_id(id)
        print(result)
        return create_success_body(result)
    except Exception as err:
        print(err)
        return create_error_body(err)
