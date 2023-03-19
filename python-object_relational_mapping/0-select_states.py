#!/usr/bin/python3
"""Task 0"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    user, passwd, db_name = args

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
