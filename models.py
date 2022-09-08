from sqlalchemy import Column, String, CHAR, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Apartment(Base):
    __tablename__ = 'apartment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    img_source = Column(String)
    bedrooms = Column(String)
    location = Column(String)
    description = Column(String)
    cost = Column(String)
    currency = Column(CHAR)
    date = Column(DateTime)

    def __repr__(self):
        return f"<Apartment {self.title}, {self.bedrooms}, {self.cost}, {self.date}>"


if __name__ == "__main__":
    
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

    with open('.config/password') as file:
        password = file.readline()

    connection = psycopg2.connect(user="postgres", password=password)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()
    sql_create_database = cursor.execute('create database dataOx')

    cursor.close()
    connection.close()

    from sqlalchemy import MetaData
    from postgress import engine

    metadata_obj = MetaData()
    metadata_obj.create_all(engine)
    Base.metadata.create_all(engine)

