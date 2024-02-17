#!/usr/bin/env python3
"""Start link class to table in database 
"""
import sys
from model_state import Base

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
                           .format(sys.argv[1], sys.argv[2]\
                                   , sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).filter(State.name.like("%a%")).all()
    for row in rows:
        print(row.id,':',row.name)