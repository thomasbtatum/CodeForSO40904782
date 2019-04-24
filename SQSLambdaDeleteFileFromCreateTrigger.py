
import json
import boto3

def lambda_handler(event, context):
    
    for record in event['Records']:
        v = json.loads(record['body'])
        for rec in v["Records"]:

            bucketName = rec["s3"]["bucket"]["name"]
            objectKey = rec["s3"]["object"]["key"]
            #print("bucket is " + bucketName + " and object is " + objectKey )
             
            sss = boto3.resource("s3")
            obj = sss.Object(bucketName, objectKey)
            obj.delete()
            
    return {
        'statusCode': 200,
        'body': json.dumps('Delete Completed.')
    }
