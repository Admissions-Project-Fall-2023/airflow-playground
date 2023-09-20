from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Dummy variable to simulate S3 interaction
mock_s3_response = {
    'Location': '/my_mock_bucket/example.txt',
    'ETag': 'mocked-etag'
}

# Function to upload a file to S3 (using the dummy variable)
def upload_to_s3():
    # Simulated S3 response
    s3_response = mock_s3_response
    
    # Processing the response (in a real scenario, we would log or use the response)
    print(f"Uploaded to: {s3_response['Location']}, ETag: {s3_response['ETag']}")

# Define the DAG
with DAG(
    'mock_aws_s3_dag',
    start_date=datetime(2023, 9, 20),
    schedule_interval=None,  # Set to None for manual execution
    catchup=False,
) as dag:
    # Define an operator that calls the S3 upload function
    s3_upload_task = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3
    )

# Define task dependencies
s3_upload_task  # There are no dependencies in this simple example
