import json
import os


def get_body(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def auth(event, _):
    if event['queryStringParameters'].get('api_key') == os.environ['PLUGIN_SECRET']:
        return {
            'principalId': 'user',
            'policyDocument': {
              'Version': '2012-10-17',
              'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': 'Allow',
                'Resource': event['methodArn']
              }]
            }
        }
    else:
        return {
            'principalId': 'user',
            'policyDocument': {
              'Version': '2012-10-17',
              'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': 'Deny',
                'Resource': event['methodArn']
              }]
            },
            'context': {
                'stringKey': 'Error. Api key invalid.'
            }
        }
