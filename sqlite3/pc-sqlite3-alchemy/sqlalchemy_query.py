from sqlalchemy_declarative import Person, Base, Address

from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Make a query to find all Persons in the database
all = session.query(Person).all()
for p in all:
    print("all {0}".format(p))

# Return the first Person from all Persons in the database
person = session.query(Person).first()
print("person {0}".format(person.name))

# Find all Address whose person field is pointing to the person object
all = session.query(Address).filter(Address.person == person).all()
print("All Address whose person field is pointing to the person object {0}".format(all))

# Retrieve one Address whose person field is point to the person object
one = session.query(Address).filter(Address.person == person).one()
print("One Address whose person field is pointing to the person object {0}".format(one))

address = session.query(Address).filter(Address.person == person).one()
print("address.post_code {0}".format(address.post_code))