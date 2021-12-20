from pymongo import MongoClient
from Connection import Connection
import re

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection
roles = db.roles


class ManageRole(Connection):
    def __init__(self, username, password=''):
        Connection.__init__(self, username, password)

    def determine_role_user(self, commande):
        test = {}
        self.commande = commande
        self.role_user = self.get_user_data_from_db["role"]
        for j in self.role_user:
            all_roles = roles.find({"Role": j})
            if all_roles:
                print("yes")
                for i in all_roles:
                    for key, values in i.items():
                        test[key] = values
                        return test

        #     if i in self.role_user:
        #         if commande == i:
        #             return f"L'utilisateur peut utiliser la commande {commande}"
        #     return f"La commande {commande} n'existe pas"
        # return f"L'utilisateur ne peut pas utiliser la commande {commande}"


a = ManageRole("Verum")
print(a.determine_role_user("METE"))
