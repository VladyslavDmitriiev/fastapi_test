from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, TIMESTAMP, ForeignKey


metadata = MetaData()

todos = Table(
    "todos",
    metadata,
    Column("id", String, primary_key=True),
    Column("title", String, nullable=False),
    Column("details", String),
    Column("isComplete", Boolean, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow)
)