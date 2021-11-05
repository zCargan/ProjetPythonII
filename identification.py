import csv

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


except FileNotFoundError:
    print("File not found")
except IOError:
    print("Error IO.")