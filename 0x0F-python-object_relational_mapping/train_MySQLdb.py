#!/usr/bin/env python3
import MySQLdb
db = MySQLdb.connect(host='localhost', user='root', password='3mod4od123321', database='hbtn_0d_tvshows')
cur = db.cursor()
cur.execute('select * from tv_genres')
print(cur.rowcount)
# for x in cur.fetchall():
#     print(x)
