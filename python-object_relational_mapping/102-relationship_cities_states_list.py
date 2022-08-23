#!/usr/bin/python3
"""Documentation"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def relationship_state_cities_state():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1],
                                  argv[2],
                                  argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State).all()
    for row in result:
        for city in row.cities:
            print(str(city.id) + ": " + city.name + " -> " + row.name)
    session.close()


if __name__ == "__main__":
    relationship_state_cities_state()
