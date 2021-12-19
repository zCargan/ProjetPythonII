import bcrypt


def check_password_strength(password):
    """
    :param password: receive a password
    :return: True if the password have minimum 8 letters, minimum a digit caractere and minimum a letter
    """
    digit = False
    letter = False
    if len(password) >= 8:
        for every_letter in password:
            if every_letter.isnumeric():
                digit = True
            if every_letter.isalpha():
                letter = True
    return digit and letter


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
    answer_in_bytes = bytes(secret_answer, encoding="utf-8")
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
