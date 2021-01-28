import sys
sys.path.append('/opt')
import json
#import service.spent_service as spent_service
from utils.http_response import create_success_body, create_error_body

def handler(event, context):
    try:#to-do: to implament filters and pagination
        #result = spent_service.get_spents(4, 5)
        #print(result)
        return create_success_body('endpoint get all tags')
    except Exception as err:
        print(err)
        return create_error_body(err)
