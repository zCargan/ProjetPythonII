from pymongo import MongoClient
from Connection import Connection

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection

user = 'test'
new_user = 'seb'

collection.replace_one({"username": user}, {'username': new_user, 'email': 'lgc.carlier@gmail.com', 'password': b'$2b$12$ON0OgajQezPDm9TZDZB.h.21/1.nz3s/ktR1mAX0rgRrtkR9Anv6m', 'secret_choice': "Your first pet's name", 'secret_answer': b'$2b$12$CghsH3XvrDG/0m8qXDsMTeKSUs0pju.2k6bG.tPslN28CEdS8u2h6', 'role': []})


#'username': 'Pipi', 'email': 'lgc.carlier@gmail.com', 'password': b'$2b$12$ON0OgajQezPDm9TZDZB.h.21/1.nz3s/ktR1mAX0rgRrtkR9Anv6m', 'secret_choice': "Your first pet's name", 'secret_answer': b'$2b$12$CghsH3XvrDG/0m8qXDsMTeKSUs0pju.2k6bG.tPslN28CEdS8u2h6', 'role': []}