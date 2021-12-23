from pymongo import MongoClient
import bcrypt


cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection
role = db.roles


class Connection:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    @property
    def check_user_exist(self):
        """
        :return: 1 if the user exist, 0 if the user dont exist
        """
        if collection.find_one({"username": self.username}):
            return True
        return False


    @property
    def get_user_data_from_db(self):
        if self.check_user_exist:
            return collection.find_one({"username": self.username})
        else:
            return False

    @property
    def check_password(self):
        if self.get_user_data_from_db:
            dic_data = self.get_user_data_from_db
            password_register_in_database = dic_data["password"]
            password_crypted = bytes(self.__password, encoding="utf-8")
            return bcrypt.checkpw(password_crypted, password_register_in_database)
        return False



