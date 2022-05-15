import json
import boto3

client = boto3.resource("dynamodb")
table = client.Table("CounterTable")
id = 1
def lambda_handler(event, context):
    
    # TODO implement
    response = table.get_item(
		Key={
			'id':id
			}
		)
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
