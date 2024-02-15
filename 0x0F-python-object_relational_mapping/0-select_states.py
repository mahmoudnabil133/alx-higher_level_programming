#!/usr/bin/python3
import sys
import MySQLdb
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM `states`")
rows = cur.fetchall()
for r in rows:
    print(r)
