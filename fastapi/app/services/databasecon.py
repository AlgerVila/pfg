from datetime import datetime, time
import psycopg2


def _executeInserts(query, bbdd: str, returnResult=None) -> list:
    conn = psycopg2.connect(
        host="192.168.1.78",
        database=bbdd,
        user="postgres",
        password="Madrid2k19")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_Answers(entityId: str, temperature: str, presure: str, timestamp: time):
    query = "INSERT INTO oriondata VALUES ('{}','{}','{}','{}')".format(
            entityId, float(temperature), float(presure), timestamp)
    _executeInserts(query, "postgres", returnResult=None)