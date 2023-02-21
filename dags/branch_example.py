### dag utilizing a branch operator
### values is passed as parameter to final python function

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
import pendulum
from datetime import timedelta # datetime

default_args = {
    "owner" : "Raul",
    "depends_on_past" : False,
    "start_date" : pendulum.datetime(2023, 2, 20),
    "retries" : 1,
    "retry_delay" : timedelta(minutes=2),
    "provide_context" : False
}

with DAG(
    "branch_test",
    default_args = default_args,
    schedule_interval = '@once',
    catchup = False) as dag:

    def my_message( msg ):
        print('Branch selected - ', msg)

    def pick_number():
        import random
        number = random.randint(1,9)
        print('number- ',number)
        if number > 5 :
            return 'greater_than'
        else:
            return 'less_than'

    task_1 = DummyOperator(
        task_id = 'task_1'
    )

    task_2 = BranchPythonOperator(
        task_id = 'pick_decision_number',
        python_callable = pick_number
    )

    task_3 = PythonOperator(
        task_id = 'less_than',
        python_callable = my_message,
        op_kwargs = { 'mmsg' : 'less_than'}
    )

    task_4 = PythonOperator(
        task_id = 'greater_than',
        python_callable = my_message,
        op_kwargs = { 'msg' : 'greater_than'}
    )

    task_1 >> task_2 >> [ task_3,task_4 ]