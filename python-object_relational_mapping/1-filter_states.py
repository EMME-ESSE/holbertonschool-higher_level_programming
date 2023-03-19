#!/usr/bin/python3
"""Task 1"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    user = args[0]
    password = args[1]
    db_name = args[2]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                   "ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
