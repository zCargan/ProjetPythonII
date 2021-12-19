from pymongo import MongoClient
from Connection import Connection
import re

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection

user = 'test'
new_user = 'seb'

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = "lolo@gl.co"

if(re.fullmatch(regex, email)):
    print("Valid Email")
else :
    print("Invalid Email")

collection.replace_one({"username": user}, {'username': new_user, 'email': 'lgc.carlier@gmail.com', 'password': b'$2b$12$ON0OgajQezPDm9TZDZB.h.21/1.nz3s/ktR1mAX0rgRrtkR9Anv6m', 'secret_choice': "Your first pet's name", 'secret_answer': b'$2b$12$CghsH3XvrDG/0m8qXDsMTeKSUs0pju.2k6bG.tPslN28CEdS8u2h6', 'role': []})


#'username': 'Pipi', 'email': 'lgc.carlier@gmail.com', 'password': b'$2b$12$ON0OgajQezPDm9TZDZB.h.21/1.nz3s/ktR1mAX0rgRrtkR9Anv6m', 'secret_choice': "Your first pet's name", 'secret_answer': b'$2b$12$CghsH3XvrDG/0m8qXDsMTeKSUs0pju.2k6bG.tPslN28CEdS8u2h6', 'role': []}