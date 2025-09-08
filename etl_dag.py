from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
import psycopg2

default_args = {
    'owner': 'gitpod',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def fetch_data():
    conn = psycopg2.connect(
        host="localhost",
        database="airflow_db",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

with DAG(
    'etl_sales_pipeline',
    default_args=default_args,
    description='ETL DAG with Postgres in Gitpod',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    create_and_insert = PostgresOperator(
        task_id="init_sales_table",
        postgres_conn_id="postgres_default",
        sql="scripts/init_db.sql"
    )

    query_data = PythonOperator(
        task_id="query_sales",
        python_callable=fetch_data
    )

    create_and_insert >> query_data
