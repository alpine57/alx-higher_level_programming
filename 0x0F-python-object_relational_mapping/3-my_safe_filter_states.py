#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == __'main'__:

db = MySQLdb.connect(host="hostname",user= sys.agv[1], passwrd=sys.agv[2], db=sys.agv[3], port=3306)
cur=db.cursor()
cur.execute( ).format(sys.agv[4])

cur.close()
db.close()
