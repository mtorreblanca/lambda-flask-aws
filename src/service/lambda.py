# https://stackoverflow.com/questions/43294802/lambda-return-payload-botocore-response-streamingbody-object-prints-but-then-emp

import boto3
import json

client = boto3.client('lambda', region_name='us-west-2')

# Print out bucket names
response = client.invoke(
    FunctionName='emit',
    InvocationType='RequestResponse',
    Payload='{}',
)

res = json.loads(response['Payload'].read())
print({'msg': res['body']})