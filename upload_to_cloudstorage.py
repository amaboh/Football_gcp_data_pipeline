import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from google.cloud import storage
from io import BytesIO
from scrapebs import *

# Set up Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'path/to/your/google-credentials.json'

# GCS client
storage_client = storage.Client()

def create_bucket(bucket_name, storage_class='STANDARD', location='us-central1'):
    """Create a new bucket in specific location with standard storage class."""
    try:
        bucket = storage_client.bucket(bucket_name)
        bucket.storage_class = storage_class
        new_bucket = storage_client.create_bucket(bucket, location=location)
        print(f"Bucket {new_bucket.name} created.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_to_gcs(bucket_name, data, file_name):
    """Upload data to a bucket in Google Cloud Storage."""
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        
        # Convert DataFrame to Arrow Table and then to Parquet
        table = pa.Table.from_pandas(data)
        parquet_buffer = BytesIO()
        pq.write_table(table, parquet_buffer)
        
        # Upload the buffer content
        blob.upload_from_string(parquet_buffer.getvalue(), content_type='application/octet-stream')
        print(f"{file_name} uploaded to {bucket_name}.")

    except Exception as e:
        print(f"Error uploading to Google Cloud Storage: {e}")

if __name__ == "__main__":
    # Set bucket name
    bucket_name = 'football_gcp_pipeline'
    
    # Create GCS bucket
    create_bucket(bucket_name)

    # Functions to process and upload
    functions = [league_table, top_scorers, detail_top, player_table, all_time_table, all_time_winner_club, top_scorers_seasons, goals_per_season]

    for func in functions:
        data = func()
        file_name = f"{func.__name__}.parquet"
        upload_to_gcs(bucket_name, data, file_name)
