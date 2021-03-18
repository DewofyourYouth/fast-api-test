from pony.orm import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()
user = getenv('USER')
password = getenv('PASSWORD')

db = Database()
db.bind(provider='postgres', user=user, password=password, host='127.0.0.1', database='postgres')


