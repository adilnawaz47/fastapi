from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *
password = "Root@123"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Root%40123@localhost:3306/fastapi"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

