# https://stackoverflow.com/questions/43294802/lambda-return-payload-botocore-response-streamingbody-object-prints-but-then-emp

import boto3

client = boto3.client('lambda', region_name='us-west-2')

# Print out bucket names
response = client.invoke(
    FunctionName='emit',
    InvocationType='RequestResponse',
    Payload='{}',
)

print(response['Payload'].read())