import asyncio

import sqlalchemy
from databases import Database
from sqlalchemy import create_engine, Column, String, Text, TIMESTAMP
from datetime import datetime

DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

feedback = sqlalchemy.Table(
    "feedback",
    metadata,
    Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    Column("language", String),
    Column("name", String),
    Column("phone_number", String),
    Column("message", Text),
    Column("created_at", TIMESTAMP, default=datetime.now),
)


engine = create_engine(DATABASE_URL)
metadata.create_all(bind=engine)


