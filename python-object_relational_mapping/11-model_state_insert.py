#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = State(name="Louisiana")
    session.add(state_name)
    session.commit()

    print(state_name.id)

    session.close()
