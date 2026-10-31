import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()

engine = create_engine(os.environ["DB_URL"])
Session_Local = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close()

