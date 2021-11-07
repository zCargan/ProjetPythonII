import csv
import os

dic_password = {}


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
                    pass
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
            else:
                print("Successful authentication, u are a simple user")
        else:
            print("incorrect password")
    else:
        print("user not found")


complete_password(dic_password)
identification(dic_password)
