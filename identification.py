import csv
import os

dic_password = {}
all_titles = []
all_privileges = []  # contains all the privileges allowed for the discord


# def search_files(folder):
#     result = os.listdir(f"..//{folder}")
#     for i in result:
#         if ".csv" not in i:
#             result.remove(i)
#     print(result)


def complete_password(dic):
    try:
        with open('Classeur1.csv') as file:
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


def identification(dic):
    user = input("What is your username?")
    if user in dic:
        password = input("What is your password?")
        if dic[user][0] == password:
            if dic[user][1] == "X":
                print("Successful authentication, u are admin too")
                print("Musique : Allowed \nLogiciel : Allowed \nMeteo : Allowed \ngestion_acces : Allowed")
            else:
                print("Successful authentication, u are a simple user")
                print("Musique : Allowed \nLogiciel : Allowed \nMeteo : Allowed \ngestion_acces : Denied")
        else:
            print("incorrect password")
    else:
        print("user not found, do u want you register?")
        new_user = input("What is your username?")
        dic_password[new_user] = []
        password_user = input("Password?")
        dic_password[new_user].append(password_user)


def define_privileges(list):
    for i in range(2, len(list)):
        # print(list[i]) // récupère les privilège
        all_privileges.append(all_titles[i])


complete_password(dic_password)
identification(dic_password)
define_privileges(all_titles)
print(dic_password)

