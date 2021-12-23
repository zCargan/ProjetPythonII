from Modérateur import Moderator
from pymongo import MongoClient
from ManageRoles import ManageRole
from Connection import Connection

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection
roles = db.roles


class Administrateur(Moderator, Connection):
    def __init__(self, username):
        self.username = username

    @property
    def admin_verify(self):
        if collection.find_one({"username": self.username}):
            return ManageRole(self.username).user_role == "Admin"
        return "User not found"

    def manage_non_admin_role(self, target, role):
        self.role = role
        if self.role == "Choose the role":
            return "Choose one choice in the list"
        self.target = target
        self.target_user = Connection(self.target, '')
        self.data_target = self.target_user.get_user_data_from_db
        if collection.find_one({"username": self.username}):
            if self.admin_verify:
                if collection.find_one({"username": self.target}):
                    target_role = collection.find_one({'username': self.target})['role']
                    if target_role != self.role:
                        self.data_target['role'] = self.role
                        collection.replace_one({"username": self.target}, self.data_target)
                        return 'The role of this user is changed'
                    return 'This user has already this role'
                return "Target user not found"
            return 'You are not an admin'
        return "Admin not found"
