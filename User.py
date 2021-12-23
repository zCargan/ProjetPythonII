from pymongo import MongoClient
from Connection import Connection

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection
roles = db.roles


class User:
    def __init__(self):
        pass

    @property
    def determine_role_user(self):
        self.role_user = roles.find({"Role": "User"})
        for i in self.role_user:
            permissions = i['Permissions']
            return permissions

    def add_role_to_user(self, role):
        self.role_user = roles.find({"Role": "User"})
        for i in self.role_user:
            self.permissions = i['Permissions']
            self.permissions.append(role)
            i["Permissions"] = self.permissions
            roles.replace_one({"Role": "User"}, i)
            return True

    def remove_role_to_user(self, role):
        self.role_user = roles.find({"Role": "User"})
        for i in self.role_user:
            self.permissions = i['Permissions']
            if role in self.permissions:
                self.permissions.remove(role)
                i["Permissions"] = self.permissions
                roles.replace_one({"Role": "User"}, i)
                return True
            return False




