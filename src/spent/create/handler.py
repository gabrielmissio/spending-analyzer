import json

# import requests


def handler(event, context):
   

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "end point create spent",
            # "location": ip.text.replace("\n", "")
        }),
    }
