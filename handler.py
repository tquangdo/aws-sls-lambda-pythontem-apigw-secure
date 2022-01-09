import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
def dtqSearch(event, context):
    if event['httpMethod'] == 'GET' and event['queryStringParameters']['query']:
        body ={
            'message': 'your query is: ' + event['queryStringParameters']['query']
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    if event['httpMethod'] == 'POST' and event['body']:
        body ={
            'message': 'received your body text',
            'msgBody': event['body']
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

    return response
