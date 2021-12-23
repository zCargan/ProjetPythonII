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

    def determine_role_user(self, commande):
        self.commande = commande
        self.role_user = self.get_user_data_from_db["role"]
        if roles.find({'Role': self.role_user}):
            for i in roles.find({'Role': self.role_user}, {"Role": 0, "Permissions": 1}):
                tab_permissions.append(i)
            print(tab_permissions)
    #        if i == self.commande:
    #            print("l'utilisateur peut exécuter cette commande !")
    #            return True
    #        print("l'utilisateur NE peut PAS exécuter cette commande !")
    #        return False

        return "Le role n'existe pas"
    # print(tab_permissions)
    # for i in tab_permissions:
    #     if i == self.commande:
    #         print("l'utilisateur peut exécuter cette commande !")
    #         return True
    #     else:
    #         print("l'utilisateur NE peut PAS exécuter cette commande !")
    #         return False


@property
def verify_permission(self, commande):
    self.role_admin = ['ADMIN', 'METEO', 'DJ', 'BAN_USER', 'BAN']
    self.role_user = ['METEO', 'DJ', 'BAN_USER']
    user = Connection.get_user_data_from_db
    roles = user.find({"role": self.role})
    return roles


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


def add_role_to_user(self):
    pass


a = ManageRole("Zink")
print(a.determine_role_user("METEO"))
