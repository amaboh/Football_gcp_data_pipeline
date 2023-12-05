# Football_gcp_data_pipeline

### Overview
This is a data pipeline which consists of scraping football data from the different wesites and ingesting into the cloud  with Google Cloud Storage and locally into PostgreSQL.

### Description
We preceed to define a series of web scraping functions with beautiful to scrape data which is converted into pandas dataframe and later into parquet format which is ingested into Google Cloud Storage which is Google's Data Lake storage service. This project is a simple implementation of data pipeline involving web scraping from a static HTML webpage and ingested into the cloud storage with no orchestration tool. 

## Get started 
- git clone repo
- cd football_gcp_data_pipeline
- python3 -m source venv .venv
- source .venv/bin/activate
- python3 -m pip install -r requirements.txt
- create a project and service account on google cloud 
- Download Google credentials and reference path in upload_to_cloud.py [export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/google-credentials.json"]
- Download PostgreSQL base on your OS: https://www.postgresql.org/download/
- run script main.py: python main.py

