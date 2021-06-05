from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

from scraping.oil_price import get_Brent_price, get_WTI_price




default_args = {
    'owner' : "Stan",
    'start_date' : datetime(2021, 4, 28),
    'retries': 0,
    'retry_delay': timedelta(seconds=5)
}


with DAG('oil_price_dag', default_args=default_args, schedule_interval="@daily", catchup=False) as dag:
    get_WTI=PythonOperator(
        task_id="S3_WTI", 
        python_callable=get_WTI_price)

    get_Brent = PythonOperator(
        task_id = 'S3_Brent',
        python_callable = get_Brent_price
    )

    [get_WTI, get_Brent]


