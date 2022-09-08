from sqlalchemy import create_engine

with open('.config/password') as file:
    password = file.readline()

engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost/dataOx_tt")
engine.connect()

print(engine)
