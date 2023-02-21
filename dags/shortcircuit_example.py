### shortcircuit operator is use to verify business logic
### if 1 or many cases are not met dag finishes
### if all conditions are met,
### https://docs.astronomer.io/learn/airflow-decorators
### https://airflow.apache.org/docs/apache-airflow/stable/operators-and-hooks-ref.html

from airflow import DAG
# from airflow.decorators import dag, task
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import ShortCircuitOperator
from pendulum import datetime
from datetime import timedelta # datetime
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    "owner" : "Raul",
    "depends_on_past" : False,
    "start_date" : datetime(2023, 2, 20, tz="UTC"),
    "retries" : 1,
    "retry_delay" : timedelta(minutes=2),
    "provide_context" : False
}

dag = DAG(
    'shortcircuit_test',
    default_args=default_args,
    schedule_interval = '@once',
    catchup=False)
def shortcircuit_fn():
    from random import randint
    numero = randint(0, 1)
    print(numero)
    return numero == 1
task_1 = DummyOperator(dag=dag, task_id='task_1')
task_2 = DummyOperator(dag=dag, task_id='task_2')
work = DummyOperator(dag=dag, task_id='work')
short = ShortCircuitOperator(dag=dag, task_id='short_circuit', python_callable=shortcircuit_fn)
final = DummyOperator(dag=dag, task_id="final", trigger_rule="all_done")

task_1 >> short >> work >> final
task_1 >> task_2 >> final

##             -->  task_2   -->
## task1                              final
##        short_circuit  -> work -->