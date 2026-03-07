from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "sohel",
    "start_date": datetime(2025,1,1)
}

dag = DAG(
    "yolo_training_pipeline",
    default_args=default_args,
    schedule_interval=None
)

train_model = BashOperator(
    task_id="train_model",
    bash_command="python train.py",
    dag=dag
)

evaluate_model = BashOperator(
    task_id="evaluate_model",
    bash_command="python test_inference.py",
    dag=dag
)

train_model >> evaluate_model