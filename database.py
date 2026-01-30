from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from file.env import SQLALCHEMY_DATABASE_URI

engine=create_engine(SQLALCHEMY_DATABASE_URI,echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
