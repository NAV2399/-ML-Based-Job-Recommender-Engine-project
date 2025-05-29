from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from model.recommender import extract_transform_load

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG('job_etl_pipeline', default_args=default_args, schedule_interval='@daily')

etl_task = PythonOperator(
    task_id='etl',
    python_callable=extract_transform_load,
    dag=dag
)

etl_task