#!/usr/bin/python3
"""Documentation"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC""", (argv[4],))
    result = cur.fetchall()
    cities = []
    for i in result:
        if i[2] == argv[4]:
            cities.append(i[1])
    print(', '.join(cities))
    cur.close()
    db.close()
