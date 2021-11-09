def connected_user(value_of_return):
    """
    this function is linked with 'identification.py'. Depending on the answer about identification.py, the return value of this function changes
    :param value_of_return: the value of the return. She determined if the user is log or not
    :return:
    return 2 if the user and the password is corrects
    return 1 if the user is correct but not the password
    return 0 if the user is unknown
    """
    if value_of_return == 2:
        message = "U are connected"
    if value_of_return == 1:
        message = "User or password incorrect"
    if value_of_return == 0:
        message = "User or password incorrect"
    return message
