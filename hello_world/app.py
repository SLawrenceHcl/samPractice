from http import client
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


    

def handler_create(event, context):
  client = boto3.client('dynamodb')
  body = json.loads(event['body'])
  data = client.put_item(
    TableName='Student',
    Item={
        'id': {
           'S': body['id']
        },
        'firstName':{
            'S': body['firstName']
        }
    }
  )
  print(data)
  response = {
      'statusCode': 200,
      'body': str(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response

def handler_getAll(event, context):
  client = boto3.client('dynamodb')
  data = client.scan(TableName='Student')
#   print(str(client.describe_table(TableName='Student')))

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
  }
  
  return response

def handler_create2(event, context):
  client = boto3.client('dynamodb')
  body = json.loads(event['body'])
  data = client.get_item(
    TableName='Student',
    Key={
        'id': {
           'S': body['id']
        }
    }
  )
  print(data)
  response = {
      'statusCode': 200,
      'body': str(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response

def handler_update(event, context):
  client = boto3.client('dynamodb')
  body = json.loads(event['body'])
  data = client.put_item(
    TableName='Student',
    Item={
        'id': {
           'S': body['id']
        },
        'firstName':{
            'S': body['firstName']
        }
    }
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  

def handler_delete(event, context):
    client = boto3.client('dynamodb')
    body = json.loads(event['body'])
    client.delete_item(
        TableName='Student',
        Key={
            'id': {
                'S': body['id']
            }
    }
    )
