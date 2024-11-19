import json

def lambda_handler(event, context):
    for record in event['Records']:
        print(f"Message: {record['body']}")

    return {
        'statusCode': 200,
        'body': json.dumps('Message processed successfully!')
    }

