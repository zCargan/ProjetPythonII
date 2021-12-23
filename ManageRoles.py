from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection
roles = db.roles


class ManageRole:
    def __init__(self, username):
        self.username = username

    @property
    def user_role(self):
        return collection.find_one({"username": self.username})["role"]

    def determine_permission(self, role_target):
        new_role_target = roles.find_one({"Role": role_target})["Permissions"]
        return new_role_target

    def show_status_user(self, target_username):
        role = ManageRole(target_username).user_role
        return "The role of " + str(target_username) + " is " + role

    def manage_role(self, role, option, new_permission):
        self.role = role
        self.option = option
        self.new_permission = new_permission
        self.actual_permission = self.determine_permission(self.role)
        if self.user_role == 'Admin':
            if option == 'remove':
                if self.new_permission not in self.actual_permission:
                    return "Not found in the permission list", False
                else:
                    self.new_permission_list = self.actual_permission
                    self.new_permission_list.remove(self.new_permission)
                    roles.replace_one({'Role': self.role}, {'Role': self.role, 'Permissions': self.new_permission_list})
                    return True
            if option == 'append':
                if self.new_permission in self.actual_permission:
                    return "This permission is already in this role"
                else:
                    self.new_permission_list = self.actual_permission
                    self.new_permission_list.append(self.new_permission)
                    roles.replace_one({'Role': self.role}, {'Role': self.role, 'Permissions': self.new_permission_list})
                    return True

