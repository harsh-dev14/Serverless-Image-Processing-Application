import json
import boto3
from PIL import Image
from io import BytesIO
import uuid
from datetime import datetime
import base64
import os

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')

def create_thumbnail(image, size=(128, 128)):
    thumbnail = image.copy()
    thumbnail.thumbnail(size)
    return thumbnail

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        image_data = body['image_data']  # Base64 encoded image data
        image_name = body.get('image_name', f'image_{uuid.uuid4()}.jpg')
        
        # Decode the image data
        img_data = base64.b64decode(image_data)
        img = Image.open(BytesIO(img_data))

        # Process the image (resize)
        img = img.resize((1280, 720))
        thumbnail = create_thumbnail(img)

        # Prepare buffers for S3
        img_buffer = BytesIO()
        img.save(img_buffer, 'JPEG')
        img_buffer.seek(0)

        thumbnail_buffer = BytesIO()
        thumbnail.save(thumbnail_buffer, 'JPEG')
        thumbnail_buffer.seek(0)

        # Retrieve S3 bucket name from environment variables
        bucket_name = os.environ.get('S3_BUCKET_NAME', 'my-image-processor-bucket')

        # Upload original image
        s3.put_object(Bucket=bucket_name, Key=f'images/{image_name}', Body=img_buffer)

        # Upload thumbnail
        s3.put_object(Bucket=bucket_name, Key=f'thumbnails/thumb_{image_name}', Body=thumbnail_buffer)

        # Save metadata to DynamoDB
        table.put_item(Item={
            'ImageID': image_name,
            'UploadDate': datetime.now().isoformat(),
            'S3Key': f'images/{image_name}',
            'ThumbnailKey': f'thumbnails/thumb_{image_name}'
        })

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Replace '*' with your frontend origin in production
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({
                'message': 'Image processed successfully',
                'image_key': f'images/{image_name}',
                'thumbnail_key': f'thumbnails/thumb_{image_name}'
            })
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Replace '*' with your frontend origin in production
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({
                'message': 'Error processing image',
                'error': str(e)
            })
        }
