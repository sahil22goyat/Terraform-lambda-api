resource "aws_s3_bucket" "my_bucket" {
  bucket = "deploybucket9466901628"
  tags = {
    Name        = "deploybucket9466901628"
    Environment = "Demo"
  }
}

resource "aws_s3_bucket_public_access_block" "block_public_access" {
  bucket = aws_s3_bucket.my_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_object" "deployment_image" {
  count = var.upload_new_image ? 1 : 0

  bucket = aws_s3_bucket.my_bucket.bucket
  key    = "deployment.png"
  source = var.deployment_image_path
  acl    = "private"

  etag = filemd5(var.deployment_image_path)
}

