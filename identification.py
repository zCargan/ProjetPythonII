import csv

dic_password = {}
all_titles = []
all_privileges = []


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
    if user in dic:
        if dic[user][3] == password:
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

