#!/usr/bin/python3
import MySQLdb
import sys

if __name__= "__main__":

db = MySQLdb.connect(host="localhost", user=sys.agv[1], passwrd=sys.agv[2], db =sys.agv[3], port=3306)
cur = db.cursor()
cur.execute("SELECT *FROM states WHERE name LIKE BINARY'{}'"
	.format(sys.agv[4]))
rows = cur.fetchall()
for rows in rows
print(row);
cur.close()
db.close()