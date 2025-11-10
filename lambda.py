import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "deploybucket9466901628"  # your existing bucket name

    try:
        # List objects in the S3 bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' not in response:
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": f"No objects found in {bucket_name}"
                })
            }

        # Get object keys
        files = [obj['Key'] for obj in response['Contents']]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "bucket": bucket_name,
                "objects": files
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }

