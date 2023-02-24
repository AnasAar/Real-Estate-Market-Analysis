from airflow.models import DAG
from airflow.operators.python import PythonOperator
from sqlalchemy_utils.types.enriched_datetime.pendulum_date import pendulum
import data_extraction as dx
import data_transformation as dt
import data_loading as dl
import modeling_analysis as ml


def initiation_processus():
    dx.init()


def airbnb_extraction():
    dx.airbnb()


def rent_extraction():
    dx.rent()


def sell_extraction():
    dx.sell()


def data_pretransforming():
    dt.pretransform()


def airbnb_transforming():
    dt.aibnb()


def rent_transforming():
    dt.rent()


def sell_transforming():
    dt.sell()


def loading_to_database():
    dl.database()


def loading_to_analysis():
    dl.annalyse()


def modeling_analysis():
    ml.statiscs()


def dashboarding():
    dl.dashboard()

with DAG(
        dag_id='RealEstate_Market_Dag',
        start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
        schedule_interval='@Daily',
        catchup=False
) as dag:
    task_initiation_processus = PythonOperator(
        task_id='initiation_processus',
        python_callable=initiation_processus,
        dag=dag
    )
    task_airbnb_extraction = PythonOperator(
        task_id='airbnb_extraction',
        python_callable=airbnb_extraction,
        dag=dag
    )
    task_rent_extraction = PythonOperator(
        task_id='rent_extraction',
        python_callable=rent_extraction,
        dag=dag
    )
    task_sell_extraction = PythonOperator(
        task_id='sell_extraction',
        python_callable=sell_extraction,
        dag=dag
    )
    task_data_pretransforming = PythonOperator(
        task_id='data_pretransforming',
        python_callable=data_pretransforming,
        dag=dag
    )
    task_airbnb_transforming = PythonOperator(
        task_id='airbnb_transforming',
        python_callable=airbnb_transforming,
        dag=dag
    )
    task_rent_transforming = PythonOperator(
        task_id='rent_transforming',
        python_callable=rent_transforming,
        dag=dag
    )
    task_sell_transforming = PythonOperator(
        task_id='sell_transforming',
        python_callable=sell_transforming,
        dag=dag
    )
    task_loading_to_database = PythonOperator(
        task_id='loading_to_database',
        python_callable=loading_to_database,
        dag=dag
    )
    task_loading_to_analysis = PythonOperator(
        task_id='loading_to_analysis',
        python_callable=loading_to_analysis,
        dag=dag
    )
    task_modeling_analysis = PythonOperator(
        task_id='modeling_analysis',
        python_callable=modeling_analysis,
        dag=dag
    )
    task_dashboard = PythonOperator(
        task_id='dashboarding_analys',
        python_callable=dashboarding,
        dag=dag
    )

task_initiation_processus >> [task_airbnb_extraction, task_rent_extraction, task_sell_extraction]\
>> task_data_pretransforming >> [task_airbnb_transforming,task_rent_transforming, task_sell_transforming]\
>> task_loading_to_database >> task_loading_to_analysis >> task_modeling_analysis >> task_dashboard
