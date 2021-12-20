from pymongo import MongoClient
from Connection import Connection

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection
roles = db.roles


class ManageRole(Connection):
    def __init__(self, username, password=''):
        Connection.__init__(self, username, password)

    def remove_role(self, role):
        self.role = role
        roles.delete_one({"Role": self.role})
        delete_from_all_user = collection.find({})
        for user in delete_from_all_user:
            for key, values in user.items():
                if key == "role":
                    self.dic_user = user
                    self.role_of_the_user = values
                    if role in self.role_of_the_user:
                        self.role_of_the_user.remove(role)
                        self.dic_user["role"] = self.role_of_the_user
                        print(type(self.role_of_the_user), self.dic_user)
                        collection.replace_one({"username": self.dic_user["username"]}, self.dic_user)
                        return True
                    else:
                        return False

    def add_role(self, role):
        self.role = role
        roles.insert_one({"Role": self.role})

    def add_role_to_user(self, myself, target):
        self.myself = myself
        self.target = target
        role_of_the_target = collection.find({"username" : self.target})["role"]
        print(role_of_the_target)

    def music_bot(self):
        list_autorized = ["ADMIN", "DJ"]

    def add_role_to_admin(self, new_role):

    def add_role_to_modo(self, new_role):

    def



a = ManageRole("bedus", "Zink")
a.add_role_to_user("DJ")
