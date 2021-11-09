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
    :return: True if the user is already in the database
    """
    dic_user = data_mongo()
    return user in dic_user


def email_already_know(email):
    """
    :param email: receive a email from the  new user
    :return: True if this email is available
    """
    available = True
    dic_user = data_mongo()
    for key, value in dic_user.items():
        if value[4] == email:
            available = False
    return not available


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


def create_data_to_db(username, first_name, last_name, email, password, password_confirmed):
    dic_user = data_mongo()
    id = number_user(dic_user)
    data = {"_id": id, "username": username, "first_name": first_name, "last_name": last_name, "email": email,
            "password": password, "password_confirmation": password_confirmed}
    collection.insert_one(data)


