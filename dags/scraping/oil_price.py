from datetime import date
import investpy
from io import StringIO
import boto3

import os

def get_Brent_price():
    ''' pushing brent price .csv to S3 bucket'''
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    #Query investpy API
    df = investpy.get_commodity_historical_data(commodity='brent oil', from_date='01/01/1980',
                                                  to_date=d1)
    
    #Connexion to your S3 bucket 
    s3 = boto3.client('s3', aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
    
    """
    Name of your bucket (it needs to be created on AWS before)
    If it is not created you can add to the code:
            # location = {'LocationConstraint': 'eu-west-3'}
            # s3.create_bucket(Bucket='bucket_name', CreateBucketConfiguration=location)
    Be sure to pick bucket-name which is available (by default it is a public bucket!)
    """
    bucket = "mybucketnameforOilScrap"

    #Turn the df into file-like object
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)

    #Pushing the the file-object 
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, 'brent.csv').put(Body=csv_buffer.getvalue())  



def get_WTI_price():
    ''' pushing WTI price .csv to S3 bucket'''
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    #Query investpy API
    df = investpy.get_commodity_historical_data(commodity='crude oil WTI', from_date='01/01/1980',
                                                  to_date=d1)
    
    
    #Connexion to your S3 bucket 
    s3 = boto3.client('s3', aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
    
    """
    Name of your bucket (it needs to be created on AWS before)
    If it is not created you can add to the code:
            # location = {'LocationConstraint': 'eu-west-3'}
            # s3.create_bucket(Bucket='bucket_name', CreateBucketConfiguration=location)
    Be sure to pick bucket-name which is available (by default it is a public bucket!)
    """
    bucket = "bucketnameOIL"
    s3 = boto3.client('s3', aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))

    #Turn the df into file-like object
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)

    #Pushing the the file-object 
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, 'WTI.csv').put(Body=csv_buffer.getvalue()) 
