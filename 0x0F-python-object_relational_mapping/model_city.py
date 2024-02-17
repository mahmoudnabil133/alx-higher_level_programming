#!/usr/bin/python3
"docs for model city"
from model_state import Base
from sqlalchemy import Column, Integer, ForeignKey, String

class City(Base):
    "class city that represent city table in database"

    __tablename__ = 'cities'
    id = Column(Integer(), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'))
