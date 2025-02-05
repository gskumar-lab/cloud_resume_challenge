import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCountTable')

def lambda_handler(event, context):
    # Get current count
    response = table.get_item(Key={'id': 'visitor_count'})
    count = response.get('Item', {}).get('count', 0)

    # Increment count
    new_count = count + 1
    table.put_item(Item={'id': 'visitor_count', 'count': new_count})

    # Return the new count
    return {
        'statusCode': 200,
        'body': json.dumps({'count': new_count}),
        'headers': {
            'Access-Control-Allow-Origin': '*',  # Enable CORS
            'Content-Type': 'application/json'
        }
    }