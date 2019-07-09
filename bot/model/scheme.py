from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    ext_user_id = Column(Integer, unique=True)
    at_date = Column(DateTime, default=datetime.utcnow)
