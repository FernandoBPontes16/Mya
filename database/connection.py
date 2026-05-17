import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

meudb = mysql.connector.connect(    
    user=os.getenv("USER_DB"),
    password=os.getenv("PASSWORD_DB"),
    host=os.getenv("HOST_DB"),
    database=os.getenv("DB_NAME"),
    port=os.getenv("DB_PORT")
)
cursor = meudb.cursor()