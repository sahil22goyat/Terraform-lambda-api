import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "deploybucket9466901628"
    key_name = "deployment.png"

    try:
        # Generate presigned URL for image (valid for 1 hour)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': key_name},
            ExpiresIn=3600  # 1 hour
        )

        response = s3.list_objects_v2(Bucket=bucket_name)
        files = [obj['Key'] for obj in response.get('Contents', [])]

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "bucket": bucket_name,
                "deployment_file": key_name,
                "deployment_url": url,
                "objects": files
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

