#!/usr/bin/python3
"""Safe fom MySQL injections"""
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
        "SELECT * FROM states WHERE BINARY name = %s"
        "ORDER BY id ASC;", (state_name,)
    )

    states = sursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
