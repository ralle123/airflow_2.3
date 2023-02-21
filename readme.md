
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
https://airflow.apache.org/docs/apache-airflow/2.3.0/start/docker.html

download
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.0/docker-compose.yaml'

mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

Initialize the database
docker compose up airflow-init

clean up environment 
docker-compose down --volumes --remove-orphans

Running airflow
docker-compose up

to see 
http://localhost:8080

login airflow
user - airflow
pass - airflow
