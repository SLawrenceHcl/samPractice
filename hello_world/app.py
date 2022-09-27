import json


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }

def lambda_handler2(event, context):
    personId=event['queryStringParameters']['personId']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "personId": personId + " from Lambda"
        }),
    }
