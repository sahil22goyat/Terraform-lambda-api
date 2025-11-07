import os
import json
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")
BUCKET = os.environ.get("BUCKET_NAME", "")
KEY = os.environ.get("IMAGE_KEY", "demo-image.jpg")
PRESIGN_EXPIRES = int(os.environ.get("PRESIGN_EXPIRES", "300"))

def lambda_handler(event, context):
    try:
        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": BUCKET, "Key": KEY},
            ExpiresIn=PRESIGN_EXPIRES
        )
    except ClientError as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}

    body = {"message": "Hello from Lambda!", "image_url": url}
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body)
    }

