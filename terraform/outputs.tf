output "api_endpoint" {
  value = aws_apigatewayv2_api.http_api.api_endpoint
}

output "lambda_name" {
  value = aws_lambda_function.demo.function_name
}

