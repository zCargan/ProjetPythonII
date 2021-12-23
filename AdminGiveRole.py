from pymongo import MongoClient
from ManageRoles import ManageRole


cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection
roles = db.roles

class AdminGiveRole(ManageRole):
    def __init__(self, admin, target):
        self.admin = admin
        self.target = target

    @property
    def manage_role_to_user(self):
        if self.show_status_user(self.admin):
            return "Bien admin"
        return "Tu n'es pas un admin pute"


