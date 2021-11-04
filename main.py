import csv
import os

dic_password = {}

try:
    with open('Classeur1.csv') as file:
        file_password = csv.reader(file, delimiter=";")
        for line in file_password:
            key = line[0]
            if key == "ï»¿user":
                pass
            else:
                if key not in dic_password:
                    dic_password[key] = []
                for i in range(1, len(line)):
                    dic_password[key].append(line[i])

    user = input("What is your username?")
    password = input("What is your password?")

    if user not in dic_password:
        print("user not found")
    elif dic_password[user][0] != password:
        print("incorrect password")
    else:
        print("Successful authentication")

except FileNotFoundError:
    print("File not found")
except IOError:
    print("Error IO.")
