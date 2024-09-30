#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Build and deploy the SAM application
sam build
sam deploy --no-confirm-changeset --no-fail-on-empty-changeset --stack-name my-serverless-app --capabilities CAPABILITY_IAM

echo "Deployment complete."
