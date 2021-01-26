import sys
sys.path.append('/opt')
import json
import service.spent_service as spent_service
from utils.http_response import create_success_body, create_error_body

def handler(event, context):
    try:#to-do: to implament filters and pagination
        id = event['pathParameters']['id']
        result = 'endpoint update spent by id {}'.format(id)#spent_service.get_spents(4, 5)
        print(result)
        return create_success_body(result)
    except Exception as err:
        print(err)
        return create_error_body(err)
