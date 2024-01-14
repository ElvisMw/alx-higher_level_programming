#!/usr/bin/python3
"""
This script lists all states from - database hbtn_0e_0_usa:
It takes 3 arguments: mysql username, mysql password
and database name (no argument validation needed)
must use the module MySQLdb (import MySQLdb)
"""
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()
        cur.execute("SELECT name FROM states")
        rows = cur.fetchall()
        for row in rows:
            print(row[0])
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        db.close()
