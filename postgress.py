from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:12345@localhost/dataOx_tt")
engine.connect()

print(engine)
