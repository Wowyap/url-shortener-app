import json
import boto3
import os
import string
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ShortUrls')

def generate_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method")
    path = event.get("rawPath", "")

    if method == "POST" and path == "/shorten":
        body = json.loads(event["body"])
        long_url = body.get("url")
        short_id = generate_id()

        table.put_item(Item={"id": short_id, "url": long_url})
        return {
            "statusCode": 200,
            "body": json.dumps({"id": short_id}),
            "headers": {"Content-Type": "application/json"}
        }

    elif method == "GET":
        short_id = path.strip("/")
        response = table.get_item(Key={"id": short_id})
        item = response.get("Item")
        if item:
            return {
                "statusCode": 301,
                "headers": {
                    "Location": item["url"]
                }
            }
        else:
            return {
                "statusCode": 404,
                "body": "Not found"
            }

    return {
        "statusCode": 400,
        "body": "Bad Request"
    }
