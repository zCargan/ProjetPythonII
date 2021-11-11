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
        return False
    else:
        return True



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
    dic_user = data_mongo()
    id = number_user(dic_user)
    data = {"_id": id, "username": username, "email": email,
            "password": password, "secret_choice": choise_question,
            "secret_answer": answer_secret_question}
    collection.insert_one(data)

