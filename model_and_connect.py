"""Models and connect to db module"""

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base

from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost:5432/alchemy_lab9"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()


class User(Base):
    """User model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)


class Post(Base):
    """Posts model"""

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))


Base.metadata.create_all(bind=engine)


App = FastAPI

if __name__ == "__main__":
    print("Hello, World!")
