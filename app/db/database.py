import mysql.connector

def get_db_connection():
    config = {
        'user': 'admin',
        'password': '1234',
        'host': '172.20.46.69',
        'database': 'clinica_db'
    }
    return mysql.connector.connect(**config)