


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url="postgresql+psycopg2://postgres:69831@localhost:5432/tested_db_123"

engine=create_engine(db_url)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)