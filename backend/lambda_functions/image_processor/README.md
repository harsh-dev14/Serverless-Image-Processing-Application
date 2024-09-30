# Image Processor Lambda Function

This Lambda function processes uploaded images by resizing them and creating thumbnails using the Pillow library. Processed images are stored in Amazon S3, and metadata is saved in DynamoDB.

## Environment Variables

- `S3_BUCKET_NAME`: Name of the S3 bucket where images are stored.

## Dependencies

- Pillow
- boto3

## Deployment

- Ensure the Pillow Layer is attached to the Lambda function.
- Deploy using AWS SAM as outlined in the top-level README.
