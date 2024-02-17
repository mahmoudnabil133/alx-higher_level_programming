#!/usr/bin/python3
"docs for file 5"
import sys
import MySQLdb
if __name__ == '__main__':
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
