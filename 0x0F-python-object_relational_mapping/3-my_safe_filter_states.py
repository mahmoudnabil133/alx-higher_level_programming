#!/usr/bin/python3
"connecting to Mysqldb"
import sys
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY states.name = %s", (sys.argv[4], )
        )
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
