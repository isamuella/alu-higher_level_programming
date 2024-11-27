#!/usr/bin/python3
"""Takes and argument and displays all values in states table"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC;".format(state_name)
    )

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
