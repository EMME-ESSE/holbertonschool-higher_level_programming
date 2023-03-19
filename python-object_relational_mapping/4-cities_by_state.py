#!/usr/bin/python3
"""task 4"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                          passwd=mysql_password, db=database_name)

    # Execute SQL query
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities"
                    "JOIN states ON cities.state_id = "
                    "states.id ORDER BY cities.id ASC")
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
