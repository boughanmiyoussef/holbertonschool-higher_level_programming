#!/usr/bin/python3
"""
Python module that lists all states from the database hbtn_0e_0_usa
Code should not be executed when imported
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=database)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")

    rows = cur.fetchall()
    for item in rows:
        print(item)

    cur.close()
    db.close()