# serverless-canonical-name-redirector
For a Serverless project that 301s from some non-canonical name to a canonical name. 
It has a rather extensive CloudFormation template in the serverless.yml file for CloudFront.

You _must_ get your ACM based certs from *us-east-1*. Don't ask.

# What
This project uses the serverless framework to deploy:
1. CloudFront Distribution ( with SSL termination ) 
1. backed by an API Gateway
2. backed by a python AWS lambda function that sends back `HTTP 301` to a canonical name

# CloudFront
