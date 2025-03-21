import json
from colorama import Fore
from encoder import encrypter


def resetData(name="", pwd="", sm=5, i=10, big=50):
    pwd = encrypter(pwd)
    dic = {
        "Name": name,
        "Password": pwd,
        "Small Points": sm,
        "Intermediate Points": i,
        "Big Points": big,
        "isProtected": False,
    }
    data = json.dumps(dic)
    file = open("settings.json", "w")
    file.write(data)
    file.close()
    print(Fore.GREEN)
    print("Settings Updated Successfully..!!")


def updateData(key, val):
    file = open("./settings.json")
    data = file.read()
    file.close()
    dic = json.loads(data)

    dic[key] = val

    data = json.dumps(dic)
    file = open("settings.json", "w")
    file.write(data)
    file.close()
    print(Fore.GREEN)
    print(key.title(), " Updated Successfully..!!")


def getData(key):
    try:
        file = open("./settings.json")
    except FileNotFoundError:
        return signup()[key]
    data = file.read()
    file.close()
    dic = json.loads(data)

    if not dic.__contains__(key):
        print(Fore.RED)
        print("Incorrect Key DO NOT TRY TO MODIFY THE CODE...!!")
        return None

    return dic[key]


def signup():
    print("Hola Amigo 🤠")
    print("It seems this is your first time")
    data = {
        "Name": "",
        "Password": "",
        "Small Points": 5,
        "Intermediate Points": 10,
        "Big Points": 50,
        "isProtected": False,
    }

    print("Let's sign you up!!")

    data["Name"] = input("Enter your name (i use anime names, so be creative) : ")
    data["Password"] = encrypter(input("Enter your password : "))

    file = open("./settings.json", "w", encoding="utf-8")

    file.write(json.dumps(data))

    file.close()
    return data
