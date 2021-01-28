import sys
sys.path.append('/opt')
import json
#import service.spent_service as spent_service
from utils.http_response import create_success_body, create_error_body

def handler(event, context):
    try:
        print(event)
        id = event['pathParameters']['id']

        #result = spent_service.get_spent_by_id(id)
        #print(result)
        return create_success_body('endpoint get tag by id')
    except Exception as err:
        print(err)
        return create_error_body(err)
