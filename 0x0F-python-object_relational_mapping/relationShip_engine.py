#!/usr/bin/env python3
"""Start link class to table in database
"""
import sys
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()

    # s1 = State(name = "california")
    # c1 = City(name = "San fransisco",state_id = 1)
    # session.add(s1)
    # session.add(c1)
    # session.commit()
