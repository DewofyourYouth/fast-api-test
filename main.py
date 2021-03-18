from fastapi import FastAPI
from pydantic import BaseModel
from database.models import insert_person, get_person_list, insert_car

app = FastAPI()


class Person(BaseModel):
    name: str
    age: int


class Car(BaseModel):
    person_id: int
    make: str
    model: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/person")
async def create_person(person: Person):
    insert_person(person.name, person.age)
    return {"message": f"Person {person.name} created!"}


@app.get("/people")
def get_people():
    people_list = get_person_list()
    return list(people_list)


@app.post("/car")
def create_car(person_id: int, make: str, model: str):
    insert_car(person_id, make, model)
    return {"message": "car created!"}
