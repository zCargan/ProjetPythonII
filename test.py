import mongo_connection
from mongo_connection import data_mongo
from function import determine_all_role

dic_user = mongo_connection.data_mongo()
collection = mongo_connection.collection


# collection.insert_one({"_id": 0, "username": "admin", "email": "admin", "password": "admin","secret_choice" : "admin", "secret_answer" : "admin", "role" : ["ADMIN"]})


def manage_roles(admin, user, option, role_modified):
    """
    this function gives this user the role given in parameter
    :param user: the user cibled by the role
    :param role_for_user: role's user
    :return: /
    """
    role_available = dic_user['admin'][6]
    role_upper = role_modified.upper()
    list_roles = determine_all_role()
    if dic_user[user][1] == 'admin':
        return ("You cant not change the admin's role")
    else:
        list_roles = determine_all_role()
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
                                    new_user_data = {"_id": id, "username": username, "email": email, "password": password,
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
                                    new_user_data = {"_id": id, "username": username, "email": email, "password": password,
                                                     "secret_choice": secret_choice, "secret_answer": secret_answer,
                                                     "role": new_users_role}
                                    collection.insert_one(new_user_data)



print(dic_user['Cargan'][6])
manage_roles('admin', 'Cargan', 'Add role', 'ff')
print(dic_user['Cargan'][6])

# user1 = {"_id": 0, "username": "Cargan", "email": "lgc.carlier@gmail.com", "password": mongo_connection.hashed_password("lolo123"),"secret_choice" : "Your first pet's name", "secret_answer" : mongo_connection.hashed_password("Peluche")}
# user2 = {"_id": 1, "username": "zink", "email": "zink@gmail.com", "password": mongo_connection.hashed_password("lolo123"),"secret_choice" : "Your first pet's name", "secret_answer" : mongo_connection.hashed_password("Peluche")}
# collection.insert_one(user1)
# collection.insert_one(user2)
