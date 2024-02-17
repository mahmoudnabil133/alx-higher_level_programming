#!/usr/bin/python3
"docs of file"
import sys
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE\
                 states.name LIKE 'N%' order by `id`")
    rows = cur.fetchall()
    for r in rows:
        if r[1][0] == 'N':
            print(r)
    cur.close()
    db.close()
