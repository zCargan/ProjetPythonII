import bcrypt
import re
from pymongo import MongoClient
import Connection

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection
role = db.roles


def check_password_strength(password):
    """
    :param password: receive a password
    :return: True if the password have minimum 8 letters, minimum a digit caractere and minimum a letter
    """
    digit = False
    letter = False
    maj = False
    temp_password = upper_function(password)
    if len(password) >= 8:
        for every_letter in password:
            if every_letter.isnumeric():
                digit = True
            if every_letter.isalpha():
                letter = True
        for i in range(0, len(password)):
            if temp_password[i] == password[i] and not temp_password[i].isnumeric():
                maj = True
    return digit and letter and maj


def upper_function(message):
    """

    :param message: a random message
    :return: the message in upper
    """
    return message.upper()


def hashed_password(password):
    """
    :param password: a password to crypt
    :return: the password crypted
    """
    if check_password_strength(password):
        password_in_bytes = bytes(password, encoding="utf-8")
        password_crypted = bcrypt.hashpw(password_in_bytes, bcrypt.gensalt())
        return password_crypted
    else:
        print("The password need to have 8characters, and min 1 letter and 1number")
        return False


def hashed_secret_answer(secret_answer):
    answer_in_bytes = bytes(upper_function(secret_answer), encoding="utf-8")
    answer_crypted = bcrypt.hashpw(answer_in_bytes, bcrypt.gensalt())
    return answer_crypted


def check_same_password(password, password_confirmed):
    return password == password_confirmed


def secret_question_ok(question, response):
    """
    :param question: the secret question choose by the user
    :param response: the reponse of this question
    :return: True if the user choose one of the question and write an answer
    """
    return ((question != "Choose your question") and (response != ""))


# def check_strength(password):
#     if len(password) >= 8:
#         if bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,15})', password)):
#             print("The password is strong")
#         elif bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,15})', password)):
#             print("The password is weak")
#     else:
#         print("You have entered an invalid password.")


def check_permission(username, commande):
    user_role = collection.find_one({"username": username})["role"]
    doc_role = role.find_one({"Role": user_role}, {"_id": 0, "Permissions": 1})
    new_commande = upper_function(commande)
    for i in doc_role["Permissions"]:
        i = upper_function(i)
        if i == new_commande:
            return f"L'utilisateur peut utiliser la commande : {commande}."
    return f"L'utilisateur NE peut PAS utiliser la commande : {commande}."

