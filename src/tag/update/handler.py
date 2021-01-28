import sys
sys.path.append('/opt')
import json
import service.spent_service as spent_service
from utils.http_response import create_success_body, create_error_body
from utils.validation import spent_validation as spent_validation

def handler(event, context):
    try:#to-do: to implament filters and pagination
        id = event['pathParameters']['id']
        payload = json.loads(event['body'])
        #print(payload)
        #spent_validation.validate(payload)
        #result = spent_service.update_spent_by_id(id, payload)
        #print(result)
        return create_success_body('endpoint update tag')
    except Exception as err:
        print(err)
        return create_error_body(err)
