import csv
from mongo_connection import check_hashed, data_mongo, collection

dic_password = {}
all_privileges = []
all_titles = []


def complete_password(dic):
    """
    complete the dictionary with all the user's information
    :param dic: take a dictionary
    :return: nothing
    """
    try:
        with open('data.csv') as file:
            file_password = csv.reader(file, delimiter=";")
            for line in file_password:
                key = line[0]
                if key == "ï»¿user":
                    for i in line:
                        all_titles.append(i)
                else:
                    if key not in dic:
                        dic[key] = []
                    for i in range(1, len(line)):
                        dic[key].append(line[i])

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Error IO.")


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
        messages = "U are connected"
    if value_of_return == 1:
        messages = "User or password incorrect"
    if value_of_return == 0:
        messages = "User or password incorrect"
    return messages


def identification_user(dic, user, password):
    """
    if the user is known and the password is correct, the user is identified with all his privileges
    the index of thing:
    [0] : id of the user
    [1] : username
    [2] : password
    [3] : secret question
    [4] : answer of this secret question

    :param dic: takes the dictionary with all users and their information
    :return:
    return 2 if the user is connected
    return 1 if the username is correct, but not the password
    return 0 if the username is incorrect

    """
    password_cryted = bytes(password, encoding="utf-8")
    if user in dic:
        if check_hashed(password_cryted, dic[user][3]):
            return 2
        else:
            return 1  # password incorrect
    else:
        return 0  # user not found


def define_privileges(list):
    """
    create a new table with all the privileges of the discord
    :param list: takes the first line of data file
    :return: nothing
    """
    for i in range(2, len(list)):
        # print(list[i]) // take the privileges
        all_privileges.append(all_titles[i])


def manage_roles(admin, user, option, role_modified):
    """
    this function gives this user the role given in parameter
    :param user: the user cibled by the role
    :param role_modified: role's user
    :return: /
    """
    dic_user = data_mongo()
    role_available = dic_user['admin'][6]
    role_upper = role_modified.upper()
    if dic_user[user][1] == 'admin':
        return ("You cant not change the admin's role")
    else:
        if admin in dic_user:
            role_of_the_admin = dic_user[admin][6]
            if 'ADMIN' in role_of_the_admin:
                if role_upper in role_available:
                    if option == "Choose do remove or add":
                        return "please choose a option"
                    elif option == "Add role":
                        for key, value in dic_user.items():
                            if key == dic_user[user][1]:
                                id = dic_user[key][0]
                                username = dic_user[key][1]
                                email = dic_user[key][2]
                                password = dic_user[key][3]
                                secret_choice = dic_user[key][4]
                                secret_answer = dic_user[key][5]
                                role = dic_user[key][6]
                                new_users_role = role
                                if role_upper in role:
                                    pass
                                else:
                                    new_users_role.append(role_upper)
                                    collection.delete_one({"_id": id})
                                    new_user_data = {"_id": id, "username": username, "email": email,
                                                     "password": password,
                                                     "secret_choice": secret_choice, "secret_answer": secret_answer,
                                                     "role": new_users_role}
                                    collection.insert_one(new_user_data)

                    else:
                        for key, value in dic_user.items():
                            if key == dic_user[user][1]:
                                id = dic_user[key][0]
                                username = dic_user[key][1]
                                email = dic_user[key][2]
                                password = dic_user[key][3]
                                secret_choice = dic_user[key][4]
                                secret_answer = dic_user[key][5]
                                role = dic_user[key][6]
                                new_users_role = role
                                if role_upper not in role:
                                    pass
                                else:
                                    new_users_role.remove(role_upper)
                                    collection.delete_one({"_id": id})
                                    new_user_data = {"_id": id, "username": username, "email": email,
                                                     "password": password,
                                                     "secret_choice": secret_choice, "secret_answer": secret_answer,
                                                     "role": new_users_role}
                                    collection.insert_one(new_user_data)


def determine_all_role():
    """

    :return: the list of all role
    """
    dic_user = data_mongo()
    all_role = dic_user["admin"][6]
    return all_role


def modify_role(you, add_remove, role):
    """
    this function change all the role list from the data base
    :param you: your username
    :param add_remove: if you will add or remove a role
    :param role: the role cibled
    :return: /
    """
    role_upper = role.upper()
    list_roles_admin = determine_all_role()
    list_roles_add = []
    list_roles_remove = []
    for i in range(0, len(list_roles_admin)):
        list_roles_add.append(list_roles_admin[i])
        list_roles_remove.append(list_roles_admin[i])
    list_roles_add.append(role_upper)
    if role_upper in list_roles_remove:
        list_roles_remove.remove(role_upper)
    dic_user = data_mongo()
    if you in dic_user:
        your_role = dic_user[you][6]
        if 'ADMIN' in your_role:
            if add_remove == "Add role":
                if role_upper in list_roles_admin:
                    return ('This role is already add')
                else:
                    id = dic_user['admin'][0]
                    username = dic_user['admin'][1]
                    email = dic_user['admin'][2]
                    password = dic_user['admin'][3]
                    secret_choice = dic_user['admin'][4]
                    secret_answer = dic_user['admin'][5]
                    new_list_role = list_roles_add
                    collection.delete_one({"_id": id})
                    new_user_data = {"_id": id, "username": username, "email": email, "password": password,
                                     "secret_choice": secret_choice, "secret_answer": secret_answer,
                                     "role": new_list_role}
                    collection.insert_one(new_user_data)
                    return ('This role is add')
            if add_remove == "Remove role":
                if role_upper in list_roles_admin:
                    id = dic_user['admin'][0]
                    username = dic_user['admin'][1]
                    email = dic_user['admin'][2]
                    password = dic_user['admin'][3]
                    secret_choice = dic_user['admin'][4]
                    secret_answer = dic_user['admin'][5]
                    new_list_role = list_roles_remove
                    collection.delete_one({"_id": id})
                    new_user_data = {"_id": id, "username": username, "email": email, "password": password,
                                     "secret_choice": secret_choice, "secret_answer": secret_answer,
                                     "role": new_list_role}
                    collection.insert_one(new_user_data)
                    return ('This role is remove')
                else:
                    return ("this role is already not available")
        else:
            return ('You are not a admin')


def search_user_role(you, username):
    dic_user = data_mongo()
    if you in dic_user:
        role_you = dic_user[you][6]
        if "ADMIN" in role_you:
            if username in dic_user:
                return dic_user[username][6]
            else:
                return ('this username is not defined')
        else:
            return ('You are not a admin')
    else:
        return ('Your username is not defined')


if __name__ == "__main__":
    user = input("What's your username?")
    password = input("What's your password?")
    complete_password(dic_password)
    identification_user(dic_password, user, password)
    message = ""
    if identification_user(dic_password, user, password) == 2:
        message = "Successful authentication, u are admin!\nMusic : Allowed \nSoftware : Allowed \nweather_report : Allowed \naccess_management : Allowed"
    elif identification_user(dic_password, user, password) == 1:
        message = "Successful authentication, u are a guest\nMusic: Allowed \nSoftware : Allowed \nweather_report : Allowed \naccess_management : Denied"
    elif identification_user(dic_password, user, password) == -1:
        message = "incorrect password"
    elif identification_user(dic_password, user, password) == 0:
        message = "user not found"
    else:
        message = "Error"
    print(message)
