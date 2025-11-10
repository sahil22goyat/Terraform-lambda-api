terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 1.3.0"
}

provider "aws" {
  region = "eu-west-1"  # Ireland
  # credentials come from AWS CLI or environment variables
}
terraform {
  backend "s3" {
    bucket         = "sjadjsinf3"   # S3 bucket you created
    key            = "terraform.tfstate"           # path to state file in bucket
    region         = "eu-west-1"
    encrypt        = true
  }
}

