#!/usr/bin/python3
"""task 3"""

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password database state_name"
              .format(args[0]))
        exit(1)

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        passwd=args[2],
        db=args[3]
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (args[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
