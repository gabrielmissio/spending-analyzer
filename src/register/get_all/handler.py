import sys
sys.path.append('/opt')
import json
import service.register_service as register_service
from utils.http_response import create_success_body, create_error_body
from utils.pagination.page_validation import page_validation, paginate_by_validation


def handler(event, context):
    try:#to-do: to implament filters and pagination
        current_page = page_validation(event)
        paginate_by = paginate_by_validation(event)

        result = register_service.get_registers(current_page, paginate_by)
        print(result)
        return create_success_body(result)
    except Exception as err:
        print(err)
        return create_error_body(err)
