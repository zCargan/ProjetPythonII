from User import User
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection
roles = db.roles


class Moderator(User):
    def __init__(self):
        pass

    @property
    def determine_role_modo(self):
        self.role_modo = roles.find({"Role": "Modérateur"})
        for i in self.role_modo:
            permissions = i['Permissions']
            return permissions

    def add_role_to_modo(self, role):
        self.role_modo = roles.find({"Role": "Modérateur"})
        for i in self.role_modo:
            self.permissions = i['Permissions']
            self.permissions.append(role)
            i["Permissions"] = self.permissions
            roles.replace_one({"Role": "Modérateur"}, i)
            return True


    def remove_role_to_modo(self, role):
        self.role_modo = roles.find({"Role": "Modérateur"})
        for i in self.role_modo:
            self.permissions = i['Permissions']
            if role in self.permissions:
                self.permissions.remove(role)
                i["Permissions"] = self.permissions
                roles.replace_one({"Role": "Modérateur"}, i)
                return True
            return False


