from Connection import Connection
import bcrypt

class PasswordForget(Connection):
    def __init__(self, username, password):
        Connection.__init__(self, username, password)


    @property
    def data_user(self):
        self.data = self.get_user_data_from_db
        return self.data

    @property
    def search_secret_question(self):
        dic_user = self.data_user
        secret_question = dic_user["secret_choice"]
        text = "Your secret question is : " + secret_question
        return text

    def check_secret_answer(self):
        secret_answer_in_database = self.data["secret_answer"]
        answer_crypted = bytes(self.__answer, encoding="utf-8")
        return bcrypt.checkpw(answer_crypted, secret_answer_in_database)

    def update_password(self, password):
        self.new_password = password
        collection



a = PasswordForget("Cargan", "Lolo1234")
print(a.data_user)