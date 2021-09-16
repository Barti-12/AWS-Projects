import json
import boto3

s3=boto3.client('s3')

def lambda_handler(event, context):
    
    bucket='somebucket'
    
    somejson= {"name":"Bartek", "age":24, "food":"kebab, pizza","free":True}
    
    fileName='testjs' + '.json'
    
    uploadFile=bytes(json.dumps(somejson).encode('UTF-8'))
    
    s3.put_object(Bucket=bucket,Key=fileName,Body=uploadFile)
    
    print("Status Ok")

