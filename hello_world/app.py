import json
from urllib import response
import boto3
import os
import uuid
from datetime import datetime

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

def createStudent(event, context):
    if('body' not in event or event['httpMethod'] != 'POST'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request not a post or no body?'})
        }  
    table_name = os.environ.get('TABLE', 'Student')
    region = os.environ.get('REGION', 'us-west-1')

    student_table = boto3.resource(
        'dynamodb',
        region_name=region
    )

    table = student_table.Table(table_name)
    activity = json.loads(event['body'])

    params = {
        'id': str(uuid.uuid4()),
        'studentName': activity['studentName']
    }

    response = table.put_student(
        TableName=table_name,
        Student=params
    )
    print(response)

    return{
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'msg': 'New Student Created'})
    }