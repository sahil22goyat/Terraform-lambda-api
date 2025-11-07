# AWS Region variable
variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
}

# S3 Bucket variable
variable "s3_bucket_name" {
  description = "Name of the S3 bucket that stores demo images"
  type        = string
}

# Lambda function name
variable "lambda_name" {
  description = "Name of the Lambda function"
  type        = string
}
