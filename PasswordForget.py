from Connection import Connection, collection
from utilities_lib import check_password_strength, upper_function, hashed_password
import bcrypt


class PasswordForget(Connection):
    def __init__(self, username, password=''):
        Connection.__init__(self, username, password)

    @property
    def data_user(self):
        if collection.find_one({"username": self.username}):
            self.data = self.get_user_data_from_db
            return self.data
        return f"{self.username} not found"

    @property
    def search_secret_question(self):
        if collection.find_one({"username": self.username}):
            dic_user = self.data_user
            secret_question = dic_user["secret_question"]
            text = "Your secret question is : " + secret_question
            return text
        return f"{self.username} not found"

    def check_secret_answer(self, answer):
        self.answer = upper_function(answer)
        secret_answer_in_database = self.data_user["secret_answer"]
        answer_crypted = bytes(self.answer, encoding="utf-8")
        return bcrypt.checkpw(answer_crypted, secret_answer_in_database)

    def update_password(self, password):
        self.password = password
        self.userdata = self.data_user
        if check_password_strength(self.password):
            self.new_password = hashed_password(password)
            self.userdata["password"] = self.new_password
            collection.replace_one({"username": self.username}, self.userdata)
            return True
        else:
            return False



