#!/usr/bin/python3
#this is a select rows from hbtn db
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], database = sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    x = c.fetchall()
    for i in x:
        print(i)
    c.close()
    db.close()
