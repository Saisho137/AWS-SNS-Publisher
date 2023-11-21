import boto3
import json

# Create a SNS client
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

sns = boto3.client(
    'sns',
    region_name='us-east-2', #Your Region
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key,
)

##Subject
subject = input("\n\Write the Subject to send: ")

#Message Body
product = input("\Enter the Product name: ")
amount = int(input("\Enter the Amount: "))
unit_price = float(input("\Enter the Unit Price: "))
total_price = amount * unit_price

#Json
message_body = {
    "Product": product,
    "Amount": amount,
    "Unit_price": unit_price,
    "Total_price": total_price
}
message_json = json.dumps(message_body)

#Send package to AWS SNS
response = sns.publish(
    TopicArn='YOUR_TOPIC_ARN',
    Message = message_json,
    Subject=subject
)

print("\n" , response)