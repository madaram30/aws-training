import os
import json
import uuid
import boto3
from PIL import Image

# Initialize the S3 client
s3_client = boto3.client('s3')

# Get processed bucket from environment variable
processed_bucket = os.environ.get('processed_bucket')
if not processed_bucket:
    raise ValueError("Environment variable 'processed_bucket' is not set.")

def lambda_handler(event, context):
    try:
        print(f"Record: {event['Records']}")
        # Loop through SQS records (only one record per event)
        for record in event['Records']:
            # Parse the SQS message body (which contains the bucket and key)
            try:
                sqs_message = json.loads(record['body'])
                print(f"SQS Message: {sqs_message}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue  # Skip this record if it cannot be parsed

            # Access the 'Records' array inside the parsed JSON and extract the bucket and key
            try:
                s3_event = sqs_message['Records'][0]  # Assuming only one record
                source_bucket = s3_event['s3']['bucket']['name']
                key = s3_event['s3']['object']['key']
            except KeyError as e:
                print(f"Missing key in the event data: {e}")
                continue  # Skip this record if the expected fields are missing

            print(f"Processing file: {key} from bucket: {source_bucket}")

            # Generate a temp name and set location for the original image
            object_key = str(uuid.uuid4()) + '-' + key
            img_download_path = f'/tmp/{object_key}'

            # Download the source image from S3 to the temp location within the Lambda execution environment
            with open(img_download_path, 'wb') as img_file:
                s3_client.download_fileobj(source_bucket, key, img_file)

            # Pixelate the image in various sizes and save to temp
            pixelate((8, 8), img_download_path, f'/tmp/pixelated-8x8-{object_key}')
            pixelate((16, 16), img_download_path, f'/tmp/pixelated-16x16-{object_key}')
            pixelate((32, 32), img_download_path, f'/tmp/pixelated-32x32-{object_key}')
            pixelate((48, 48), img_download_path, f'/tmp/pixelated-48x48-{object_key}')
            pixelate((64, 64), img_download_path, f'/tmp/pixelated-64x64-{object_key}')

            # Upload the pixelated versions to the processed bucket
            s3_client.upload_file(f'/tmp/pixelated-8x8-{object_key}', processed_bucket, f'pixelated-8x8-{key}')
            s3_client.upload_file(f'/tmp/pixelated-16x16-{object_key}', processed_bucket, f'pixelated-16x16-{key}')
            s3_client.upload_file(f'/tmp/pixelated-32x32-{object_key}', processed_bucket, f'pixelated-32x32-{key}')
            s3_client.upload_file(f'/tmp/pixelated-48x48-{object_key}', processed_bucket, f'pixelated-48x48-{key}')
            s3_client.upload_file(f'/tmp/pixelated-64x64-{object_key}', processed_bucket, f'pixelated-64x64-{key}')

        return {
            'statusCode': 200,
            'body': json.dumps('Successfully processed SQS message')
        }

    except Exception as e:
        print(f"Error processing SQS message: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }

def pixelate(pixelsize, image_path, pixelated_img_path):
    try:
        img = Image.open(image_path)
        temp_img = img.resize(pixelsize, Image.BILINEAR)
        new_img = temp_img.resize(img.size, Image.NEAREST)
        new_img.save(pixelated_img_path)
    except Exception as e:
        print(f"Error in pixelation: {str(e)}")
