import json
from colorama import Fore
from crypt import encrypter

def resetData(name="Half Blood Prince", pwd = "Shinigami", sm = 5, i = 10, big = 50):
    pwd = encrypter(pwd)
    dic = {"Name":name, "Password": pwd, "Small Points":sm,"Intermediate Points":i, "Big Points":big, 'isProtected':False}
    data = json.dumps(dic)
    file = open('settings.json','w')
    file.write(data)
    file.close()
    print(Fore.GREEN)
    print("Settings Updated Successfully..!!")

def updateData(key, val):
    file = open('./settings.json')
    data = file.read()
    file.close()
    dic = json.loads(data)

    dic[key] = val

    data = json.dumps(dic)
    file = open('settings.json','w')
    file.write(data)
    file.close()
    print(Fore.GREEN)
    print(key.title()," Updated Successfully..!!")

def getData(key):
    file = open('./settings.json')
    data = file.read()
    file.close()
    dic = json.loads(data)

    if not dic.__contains__(key):
        print(Fore.RED)
        print("Incorrect Key DO NOT TRY TO MODIFY THE CODE...!!")
        return None
    
    return dic[key]