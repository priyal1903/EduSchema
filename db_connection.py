
import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="priyal1903",
        database="EduSchema"
    )
    return connection
