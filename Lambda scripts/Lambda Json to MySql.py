import json
import boto3
import urllib
import pymysql

#connection setup
endpoint= '**************.rds.amazonaws.com'
username=username
password=password
database_name=database_name

#creating connection to RDS MySql  
connection=pymysql.connect(host=endpoint, user=username, password=password, db=database_name)
cursor=connection.cursor()

s3=boto3.client('s3')


def lambda_handler(event, context):
   
    bucket='simplebucket' #selected bucket
    key='data1/states.json' # some json file
    
    response=s3.get_object(Bucket=bucket,Key=key)
    
    content=response['Body']
    json_obj=json.loads(content.read())
    
    for value in json_obj['states']:
        state_name=value["name"]
        ab_code=value['abbreviation']
        area_code=str(value['area_codes'])
        
    
        cursor.execute("INSERT INTO States(name, ab_code, area_code) VALUES (%s, %s, %s)",(state_name,ab_code,area_code))
    connection.commit()
     

    
    
    
    
