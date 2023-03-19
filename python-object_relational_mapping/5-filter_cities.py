#!/usr/bin/python3
"""Task 5"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name"
              .format(sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id"
                " = states.id WHERE states.name = %s ORDER BY cities.id ASC",
                  (state_name,))

    cities = []
    for row in cur.fetchall():
        cities.append(row[0])

    print(", ".join(cities))

    cur.close()
    conn.close()

