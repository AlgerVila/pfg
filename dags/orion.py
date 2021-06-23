from datetime import date

from airflow.operators.python import task


try:

    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import requests
    import json
    print("All Dag Modules are ok ----")
except Exception as e:
    print("Error {} ".format(e))


def postInfo():
    urlFiware = "http://172.19.0.5:1026/v2/entities/Street1"
    headers = {'Content-Type': 'application/json'}
    urlFastAPi = "http://192.168.1.78:5000/update/entity"

    info = requests.get(urlFiware).json()
    print(info)
    r = requests.post(url=urlFastAPi, data=json.dumps(info), headers=headers)
    return r.status_code

# */1 * * * * Execute every minute
with DAG(
    dag_id="orion",
    schedule_interval=" */3 * * * * ",
    default_args={
        "owner": "airflow",
        "retries": 0,
        "retry_delay": timedelta(minutes=5),
        "start_date": datetime(2021,6,19)
    },
    catchup = False) as f:

    getInfoFromFiware = PythonOperator(
        task_id= "postInfo",
        python_callable=postInfo
    )