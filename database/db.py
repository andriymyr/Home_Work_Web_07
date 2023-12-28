from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import configparser
import pathlib

file_config = pathlib.Path(__file__).parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

# print("-------------", file_config)

username = config.get("DB", "user")
password = config.get("DB", "password")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")

url = f"postgresql://{username}:{password}@{domain}:5432/{db_name}"
Base = declarative_base()
engine = create_engine(url, echo=True, pool_size=5)

Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()
