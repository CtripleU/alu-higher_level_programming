#!/usr/bin/python3
"""Documentation"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    result = cur.fetchall()
    for i in result:
        if i[1][0] == 'N':
            print(i)
    cur.close()
    db.close()
