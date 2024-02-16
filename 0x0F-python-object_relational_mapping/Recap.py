#!/usr/bin/python3
import MySQLdb
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
###########################  mysqldb  ##############################################
#!/usr/bin/env python3
""
import sys
import MySQLdb
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("""
            SELECT states.id, states.name, cities.name
            FROM states INNER JOIN cities ON states.id = cities.state_id
            WHERE states.name = %s
            """, (sys.argv[4], ))
rows = cur.fetchall()
for r in rows:
    print(r)
############################ sqlalchemy   #########################################################
engine = create_engine("mysql+mysqldb://root:3mod4od123321@localhost/hbtn_0e_6_usa")#, echo=True)
Base = declarative_base()

class State(Base):
    """ class represent the states table in database """

    __tablename__='states'
    id = Column(Integer(),primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

rows = session.query(State).all()
for row in rows:
    print(row.id,':',row.name)
