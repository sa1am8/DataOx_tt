from sqlalchemy import create_engine

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="postgres", password="1111")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()
sql_create_database = cursor.execute('create database sqlalchemy_tuts')

cursor.close()
connection.close()


engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/mydb")
engine.connect()
print(engine)