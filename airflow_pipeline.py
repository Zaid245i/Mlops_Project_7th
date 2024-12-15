from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def collect_data():
    os.system('python fetch_data.py')  # Python script for data collection

def preprocess_data():
    os.system('python preprocess_data.py')  # Python script for data preprocessing

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 1),
    'retries': 1
}

with DAG('weather_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    collect_task = PythonOperator(
        task_id='collect_data',
        python_callable=collect_data
    )

    preprocess_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data
    )

    collect_task >> preprocess_task
