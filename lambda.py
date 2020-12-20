import json

def respond(msg, status=200):
    return {
        'statusCode': str(status),
        'body': msg,
        'headers': {},
    }

def lambda_handler(event, context):        
    return respond("hello world", status=200)
