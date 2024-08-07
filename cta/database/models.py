from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    tg_id = Column(Integer, unique=True, nullable=False)

    alias = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    xp = Column(Integer)
    city = Column(String)
    univer = Column(String)
    card_id = Column(Integer)

    web = Column(Integer)
    rev = Column(Integer)
    pwn = Column(Integer)
    crypto = Column(Integer)
    ppc = Column(Integer)
    forensic = Column(Integer)
    pentest = Column(Integer)
