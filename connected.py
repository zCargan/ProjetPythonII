from identification import identification_user


def connected(dic, user, password):
    """
    return a message about the connection or not for the user, and the eventually error
    :param dic: take a dictionary with the ensemble of users and password
    :param user: take the username introduced by the user
    :param password: take the password introduced by the user
    :return: nothing
    """
    message = ""
    if identification_user(dic, user, password) == 2:
        message = "Successful authentication, u are admin!"
#"\nMusic : Allowed \nSoftware : Allowed \nweather_report : Allowed \naccess_management : Allowed"
    elif identification_user(dic, user, password) == 1:
        message = "Successful authentication, u are a guest"
#"\nMusic: Allowed \nSoftware : Allowed \nweather_report : Allowed \naccess_management : Denied"
    elif identification_user(dic, user, password) == -1:
        message = "incorrect password"
    elif identification_user(dic, user, password) == 0:
        message = "user not found"
    else:
        message = "Error"
    return message
