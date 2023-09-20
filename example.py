from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import boto3
from moto import mock_s3

# Function to upload a file to S3
def upload_to_s3():
    # Mocked S3 client using moto
    s3_client = boto3.client('s3', region_name='us-east-1')
    
    # Mock bucket name
    bucket_name = 'my_mock_bucket'
    
    # Define the contents of the file to be uploaded
    file_contents = b"Hello, mock S3!"
    
    # Specify the object key
    object_key = 'example.txt'
    
    # Upload the file to the mock S3 bucket
    s3_client.create_bucket(Bucket=bucket_name)
    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=file_contents)
    
    print(f"Uploaded '{object_key}' to '{bucket_name}'")

# Define the DAG
with DAG(
    'mock_aws_s3_dag',
    start_date=datetime(2023, 9, 20),
    schedule_interval=None,  # Set to None for manual execution
    catchup=False,
) as dag:
    # Mock AWS S3 using moto
    with mock_s3():
        # Define an operator that calls the S3 upload function
        s3_upload_task = PythonOperator(
            task_id='upload_to_s3',
            python_callable=upload_to_s3
        )

# Define task dependencies
s3_upload_task  # There are no dependencies in this simple example
