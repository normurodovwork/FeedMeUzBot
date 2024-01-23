import asyncio

import sqlalchemy
from databases import Database
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./FeedMe.db"
database = Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = create_engine(DATABASE_URL)
metadata.create_all(bind=engine)