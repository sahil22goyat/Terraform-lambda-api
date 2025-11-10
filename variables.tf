variable "region" {
  default = "eu-west-1"
}

variable "upload_new_image" {
  description = "Set to true to upload a new deployment image"
  type        = bool
  default     = false
}

variable "deployment_image_path" {
  description = "Path to the local deployment image to upload"
  type        = string
  default     = "deployment.png"
}

