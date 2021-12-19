from pymongo import MongoClient
import bcrypt

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection


class Connection:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def __str__(self):
        return f"Bonjour {self.username}"

    @property
    def check_user_exist(self):
        """
        :param username: the username of the user
        :return: 1 if the user exist, 0 if the user dont exist
        """
        users_elements = 0
        for i in collection.find({"username": self.username}):
            users_elements = + 1
        if users_elements > 0:
            return True
        else:
            return False

    @property
    def get_user_data_from_db(self):
        if self.check_user_exist:
            user_data = {}
            data = collection.find({"username": self.username})
            for i in data:
                for key, value in i.items():
                    user_data[key] = value
            return True, user_data
        else:
            return False

    @property
    def check_password(self):
        dic_data = self.get_user_data_from_db
        password_register_in_database = dic_data["password"]
        password_crypted = bytes(self.__password, encoding="utf-8")
        return bcrypt.checkpw(password_crypted, password_register_in_database)
