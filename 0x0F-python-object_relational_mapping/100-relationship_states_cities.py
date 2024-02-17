#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s1 = State(name="California")
    c1 = City(name="San Francisco")

    c1.state = s1
    session.add(c1)
    session.commit()
