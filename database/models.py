from pony.orm import *
from database import db


class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set("Car")


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)


sql_debug(True)
db.generate_mapping(create_tables=True)


@db_session
def insert_person(name, age):
    Person(name=name, age=age)
    commit()
    print(f'Person: {name} created!')


@db_session
def print_person_name(person_id):
    p = Person[person_id]
    print(p.name)


@db_session
def get_person_list():
    people = select(p.name for p in Person)[:]
    return people


@db_session
def insert_car(person_id, make, model):
    person = Person[person_id]
    Car(make=make, model=model, owner=person)
