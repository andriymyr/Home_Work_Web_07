from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import sqlalchemy.exc
import configparser
import pathlib
import sys

file_config = pathlib.Path(__file__).parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)


username = config.get("DB", "user")
password = config.get("DB", "password")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")

url = f"postgresql://{username}:{password}@{domain}:5432/{db_name}"
Base = declarative_base()
engine = create_engine(url, echo=True, pool_size=5)

try:
    Base.metadata.create_all(engine)
except sqlalchemy.exc.OperationalError:
    print(f"\n", "=" * 30, f"\n", "Немає конекту до бази даних", f"\n", "=" * 30)
    sys.exit()

DBSession = sessionmaker(bind=engine)
session = DBSession()
