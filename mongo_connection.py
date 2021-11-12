import bcrypt
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://Logan:lolo123@cluster0.igyjs.mongodb.net/ecole?retryWrites=true&w=majority")
db = cluster.testdb
collection = db.testcollection


def data_mongo():
    """
    this function complete the 'dic_mongo' with the {'username' : ['all the user element']} and return it
    :return: the dictionary complete
    """
    dic_mongo = {}
    results = collection.find({})
    for result in results:
        user = result["username"]
        dic_mongo[user] = []
        for key, value in result.items():
            dic_mongo[user].append(value)
    return dic_mongo


def number_user(dic):
    """
    define the number of user already exist in database
    :param dic:
    :return: the lenght of the dictonary, the number of users
    """
    return len(dic)


def user_already_know(user):
    """
    :param user: a user
    :return: False if the user is already not in the database
    """
    dic_user = data_mongo()
    return user in dic_user


def email_ok(email):
    """
    :param email: receive a email from the  new user
    :return: False if this email is available
    """
    in_dic = False
    email_incorrect = True
    number_at = 0
    dic_user = data_mongo()
    for key, value in dic_user.items():
        if value[4] == email:
            in_dic = True
    for i in range(0, len(email)):
        if email[i] == "@":
            number_at += 1
    if number_at == 1:
        email_incorrect = False

    if in_dic == False and email_incorrect == False:
        return True
    else:
        return False


def same_password(password, password_confirm):
    """
    :param password: the first input password of the user
    :param password_confirm: the second input password of the user
    :return: True if the passwords are the same
    """
    return password == password_confirm


def is_strong_password(password):
    """
    :param password: receive a password
    :return: True if the password have minimum 8 letters, minimum a digit caractere and minimum a letter
    """
    digit = False
    letter = False
    # containsymbole = False
    if len(password) >= 8:
        for every_letter in password:
            if every_letter.isnumeric():
                digit = True
            if every_letter.isalpha():
                letter = True
            # if not (lettre.isalnum()):
            #     containsymbole = True
    return digit and letter


def secret_question_ok(question, response):
    """
    :param question: the secret question choose by the user
    :param response: the reponse of this question
    :return: True if the user choose one of the question and write an answer
    """
    return ((question != "Choose your question") and (response != ""))


def hashed_password(password):
    """
    :param password: a password to crypt
    :return: the password crypted
    """
    password_in_bytes = bytes(password, encoding="utf-8")
    password_crypted = bcrypt.hashpw(password_in_bytes, bcrypt.gensalt())
    return password_crypted


def check_hashed(password_from_database, password_crypted):
    return bcrypt.checkpw(password_from_database, password_crypted)


def defined_id_user():
    """
    define the id of the new user
    :return: the id of the new user
    """
    dic_user = data_mongo()
    new_id = 0
    for key, value in dic_user.items():
        if value[0] >= new_id:
            new_id = value[0] + 1
    return new_id


def change_password_user(user, password):
    """
    change the password of the user into the database
    :param user: the username that we delete from the databse
    :param password: the new password introduce by the user
    :return: /
    """
    dic_user = data_mongo()
    new_user_data = {}
    for key, values in dic_user.items():
        if dic_user[key][1] == user:
            id = dic_user[key][0]
            username = dic_user[key][1]
            email = dic_user[key][2]
            secret_choice = dic_user[key][4]
            secret_answer = dic_user[key][5]
            collection.delete_one({"_id": id})
            new_password = hashed_password(password)
            new_id = defined_id_user()
            new_user_data = {"_id": new_id, "username": username, "email": email, "password": new_password,
                             "secret_choice": secret_choice, "secret_answer": secret_answer, "role": []}
    collection.insert_one(new_user_data)




def create_data_to_db(username, email, password, choise_question, answer_secret_question):
    """
    encode the user's datas into the databse
    :param username: username from the user
    :param email: email from the user
    :param password: password from the user
    :param choise_question: secret from the user
    :param answer_secret_question: answer from the user
    :return: /
    """
    role = []
    id = defined_id_user()
    data = {"_id": id, "username": username, "email": email,
            "password": hashed_password(password), "secret_choice": choise_question,
            "secret_answer": hashed_password(answer_secret_question), "role": role}
    collection.insert_one(data)
