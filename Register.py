from utilities_lib import check_password_strength, upper_function, hashed_password, hashed_secret_answer, \
    check_same_password, secret_question_ok
from Connection import Connection, collection
import re


class Register:
    def __init__(self, username, password, password_confirmed, email, secret_question, secret_answer):
        self.username = username
        self.password = password
        self.password_confirmed = password_confirmed
        self.email = email
        self.secret_question = secret_question
        self.secret_answer = upper_function(secret_answer)

    @property
    def check_email_exist(self):
        """
        check if email address exist
        :return: True if the email is correct and if it exist in the database, False if the email address does exist in
        the database and Invalid Email if the email address is not valid
        """
        users_elements = 0
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, self.email):
            for i in collection.find({"email": self.email}):
                users_elements = + 1
            if users_elements > 0:
                return True
            return False
        else:
            return "Invalid Email"

    @property
    def check_user_exist(self):
        """
        :return: True if the user exist in the data
        """
        users_elements = 0
        if self.username != "":
            for i in collection.find({"username": self.username}):
                users_elements = + 1
            if users_elements > 0:
                return True
            else:
                return False
        return "Vous devez entrer un Username !", False

    @property
    def insert_user_data_to_db(self):
        """

        :return: Welcome + the username if the creation of the account is successful
        """
        if not self.check_user_exist:
            if not self.check_email_exist:
                if check_password_strength(self.password):
                    if check_same_password(self.password, self.password_confirmed):
                        if secret_question_ok(self.secret_question, self.secret_answer):
                            role = "User"
                            data = {"username": self.username, "email": self.email,
                                    "password": hashed_password(self.password), "secret_question": self.secret_question,
                                    "secret_answer": hashed_secret_answer(self.secret_answer), "role": role}
                            collection.insert_one(data)
                            return f"Welcome {self.username}"
                        return "Question or/and answer null"
                    return "Different passwords"
                return "Password need to have a character, a letter, a maj and 8 char min"
            return "This email address already exists/invalid"
        return "This username already exists/invalid"

