import datetime
from colorama import Fore
import normal
import os
import pyinputplus as pyip
import settingsData as settings
import encoder
from database import *


db_obj = DB()
logged_user = None

ACQ_STATUS = 1





def getScore():
    fs = open("tasks.txt", "r")
    lines = fs.readlines()
    fs.close()
    return len(lines)


def checkReward():
    score = getScore()
    print(Fore.LIGHTGREEN_EX)
    print("-" * 20)
    if score % 5 == 0:
        gainZeroReward()
        print("🥳 MINI REWARD GAINED 🥳 ")
    if score % 100 == 0:
        gainTwoReward()
        print("🥳 🥳 🥳 LARGE REWARD 🥳🥳 🥳  ")
    if score % 10 == 0:
        gainOneReward()
        print("🥳 🥳  INTERMEDIATE REWARD GAINED 🥳 🥳 ")
    print("-" * 20)


def addTask(task, points):
    db_obj.add_task(task, points, logged_user)
    print(Fore.LIGHTGREEN_EX)
    print("-" * 20)
    print("Task Added Successfully..!!")
    print("-" * 20)
    score = db_obj.get_points(logged_user)
    print("Total Score : ", score)
    checkReward()


def displayTasks():
    tasks = db_obj.get_tasks()
    print(Fore.YELLOW)
    print("-" * 20)
    print("Your Total Tasks : ", getScore())
    i = 1
    print("-" * 20)
    for task in tasks:
        print(i, ". ", task[1])
        print("POINTS : ", task[3])
        i += 1


def clearTasks():
    print(Fore.RED)
    pwd = encoder.enencoderer(pyip.inputPassword("Enter The Password : "))
    if pwd == db_obj.get_password(logged_user):
        db_obj.delete_tasks(logged_user)
        print("All Tasks Deleted Successfully..!!")
        print("-" * 20)
    else:
        print("Didn't Deleted Any Data Cause of Incorrect Password..!!")


def displayAcquiredReward():
    i = 1
    print("-" * 30)

    for reward in db_obj.get_rewards_by_status(logged_user, ACQ_STATUS):
        print(i, " . ", reward[1])
        print("Points : ", reward[2])
        print("-" * 30)


def addSeriesReward():
    # TODO : Add Series Here
    name = input("Enter the name of series : ")
    start = int(input("Starting Episode : "))
    end = int(input("Ending Episode : "))
    for i in range(start, end + 1):
        addRewardToFile("episodes.txt", f"{name}--{i}")


def addReward():
    # TODO : Add Rewards Here
    # addRewardToFile(file, mov)
    ch = rewardMenu()

    if ch == 1:
        print("Enter the Small Rewards (wqz for quit) ")
        while True:
            rew = input("Enter The Reward : ").title()
            if rew == "wqz".title():
                print(Fore.LIGHTGREEN_EX)
                print("All Small Rewards Has Been Added..!!")
                return None
            if rew == "":
                print(Fore.RED)
                print("Enter the Reward Name..!!")
                continue
            addRewardToFile("smallReward.txt", rew)
    if ch == 2:
        print("Enter the Intermediate Rewards (wqz for quit) ")
        while True:
            rew = input("Enter The Reward : ").title()
            if rew == "wqz".title():
                print(Fore.LIGHTGREEN_EX)
                print("All Intermediate Rewards Has Been Added..!!")
                return None
            if rew == "":
                print(Fore.RED)
                print("Enter the Reward Name..!!")
                continue
            addRewardToFile("interReward.txt", rew)
    if ch == 3:
        print("Enter the Big Rewards (wqz for quit) ")
        while True:
            rew = input("Enter The Reward : ").title()
            if rew == "wqz".title():
                print(Fore.LIGHTGREEN_EX)
                print("All Big Rewards Has Been Added..!!")
                return None
            if rew == "":
                print(Fore.RED)
                print("Enter the Reward Name..!!")
                continue
            addRewardToFile("bigReward.txt", rew)


def gainZeroReward():
    # TODO : Gain Reward
    reward = removeFirstLine("smallReward.txt")
    reward = f"Your Level 0 Reward is : {reward}"
    rewardFile = open("rewards.txt", "a+")
    rewardFile.write(reward)
    rewardFile.close()
    print(Fore.LIGHTGREEN_EX)
    print("Reward : " + reward)


def gainOneReward():
    # TODO : Gain Reward
    reward = removeFirstLine("./intermediateReward.txt")
    reward = f"Your Level 1 Reward is : {reward}"
    rewardFile = open("rewards.txt", "a+")
    rewardFile.write(reward)
    rewardFile.close()
    print(Fore.LIGHTGREEN_EX)
    print("Reward : " + reward)


def gainTwoReward():
    # TODO : Gain Reward
    reward = removeFirstLine("./bigReward.txt")
    reward = f"Your Level 2 Reward is : {reward}"
    rewardFile = open("rewards.txt", "a+")
    rewardFile.write(reward)
    rewardFile.close()
    print(Fore.LIGHTGREEN_EX)
    print("Reward : " + reward)


def rewardMenu():
    print(Fore.MAGENTA)
    normal.printBrand("Reward Settings", Fore.MAGENTA)
    print("1. Small Reward")
    print("2. Medium Reward")
    print("3. Big Reward")
    try:
        i = int(input("Enter the choice : "))
        if i > 3:
            raise Exception("In")
    except Exception:
        print(Fore.RED)
        print("Enter correct options")
    else:
        return i


def configMenu():
    while True:
        print(Fore.WHITE)
        normal.printBrand("Settings", Fore.WHITE)
        print("1. Add Reward")
        print("2. Delete All Rewards")
        print("3. View Upcoming Reward")
        print("4. Account Settings")
        print("5. Back to Main Menu")
        print()
        ch = input("Enter the option : ")

        if ch == "1":
            addReward()
        elif ch == "2":
            deleteReward()
        elif ch == "3":
            viewReward()
        elif ch == "4":
            accountMenu()
        elif ch == "5":
            print("Taking Back.....")
            return None
        else:
            print(Fore.LIGHTRED_EX)
            print("Enter Above Options Mate")


def removeFirstLine(filename):
    # TODO : Remove First Line
    try:
        file = open(filename, "r")
    except:
        print(Fore.RED)
        print("No Rewards Set, Please Set Reward in 'Settings'")
        return None
    lines = file.readlines()
    file.close()
    # print(lines)
    file = open(filename, "w")
    ch = lines[0]
    for line in lines:
        if line == lines[0]:
            continue
        else:
            file.write(line)
    file.close()
    return ch


def addRewardToFile(filename, text):
    rewardFile = open(filename, "a+")
    rewardFile.writelines([text + "\n"])
    rewardFile.close()


def viewReward():
    normal.printBrand("SMALL REWARDS", Fore.YELLOW, "-")
    readFileReward("./smallReward.txt")
    print()
    normal.printBrand("MEDIUM REWARDS", Fore.YELLOW, "-")
    readFileReward("./interReward.txt")
    print()
    normal.printBrand("BIG REWARDS", Fore.YELLOW, "-")
    readFileReward("./bigReward.txt")
    print()


def deleteReward():
    print(Fore.RED)
    print("Type swarup@rewardia")
    if input() != "swarup@rewardia":
        print(Fore.RED)
        print("Failed..!!")
        return None

    print("Enter your Password..!!")
    if encoder.enencoderer(pyip.inputPassword()) != settings.getData("Password"):
        print(Fore.RED)
        print("Incorrect Password..!!")
        return None

    ch = rewardMenu()
    print(Fore.LIGHTGREEN_EX)
    if ch == 1:
        os.unlink("./smallReward.txt")
        print("Deleted Successfully..!!")
    elif ch == 2:
        os.unlink("./interReward.txt")
        print("Deleted Succesfully..!!")
    elif ch == 3:
        os.unlink("./bigReward.txt")
        print("Deleted Successfully..!!")


def readFileReward(fileName):
    try:
        file = open(fileName, "r")
        lines = file.readlines()

        print("Number of Records Found : ", len(lines))
        i = 1
        for line in lines:
            print(f"{i}. {line}")
            i += 1
        print()
        file.close()
    except:
        print("Number Of Records : 0")


def accountMenu():
    normal.printBrand("Account Menu", Fore.YELLOW)
    ch = normal.myMenu(
        [
            "View Account Details",
            "Change Username",
            "Change Password",
            "Change Point System",
            "Toggle Login Protection",
            "Reset Account",
            "Back",
        ],
        Fore.YELLOW,
    )

    if ch == 1:
        displayData()
    if ch == 2:
        print("Enter New Username : ")
        user = input()
        re = input("Confirm Username : \n")

        if re != user:
            print(Fore.RED)
            print("Mismatch Error")
            return None
        settings.updateData("Name", user)
        print(Fore.GREEN)
        print("Successfully Changed Username..!!")
    if ch == 3:
        changePassword()
    if ch == 4:
        pass
    if ch == 5:
        toggleProtection()
    if ch == 6:
        settings.resetData()
    if ch == 7:
        return None


def displayData():
    normal.printBrand("User Details", Fore.LIGHTCYAN_EX, ".")

    user = settings.getData("Name")
    pwd = settings.getData("Password")
    sm = settings.getData("Small Points")
    inte = settings.getData("Intermediate Points")
    big = settings.getData("Big Points")

    print(f"Username : {user}")
    print(f"Points for Having Level 0 Rewards : {sm}")
    print(f"Points for Having Level 1 Rewards : {inte}")
    print(f"Points for Having Level 2 Rewards : {big}")


def changePassword():
    cur = input(
        "Enter the current password ('Shinigami' if you are changing for 1st Time) : \n"
    )

    getpwd = settings.getData("Password")
    cur = encoder.enencoderer(cur)

    if cur != getpwd:
        print(Fore.RED)
        print("Incorrect Password : ")
        return None

    pwd = encoder.enencoderer(input("Enter the New Password : \n"))
    re = encoder.enencoderer(input("Re-enter the password : \n"))

    if re != pwd:
        print(Fore.RED)
        print("Error : Password and Re-entered Password Are Mis-matched..!!")
        return None
    settings.updateData("Password", pwd)

    print(Fore.LIGHTGREEN_EX)
    print("Successfully Changed Password..!!")


def isProtected():
    return settings.getData("isProtected")


def changePoints():
    try:
        a = int(input("Enter the points for Level 0 Reward : "))
        b = int(input("Enter the points for Level 1 Reward : "))
        c = int(input("Enter the points for Level 2 Reward : "))
    except ValueError:
        print(Fore.RED)
        print("Error : Enter digit..!!")
        return None

    settings.updateData("Small Points", a)
    settings.updateData("Intermediate Points", b)
    settings.updateData("Big Points", c)

    print(Fore.LIGHTGREEN_EX)
    print("Successfully Updated Your Point System..!!")


def toggleProtection():
    cur = input("Enter the password : \n")

    getpwd = settings.getData("Password")
    cur = encoder.enencoderer(cur)

    if cur != getpwd:
        print(Fore.RED)
        print("Incorrect Password : ")
        return None

    if not isProtected():
        settings.updateData("isProtected", True)
        print(Fore.LIGHTGREEN_EX)
        print("Login Protection Enabled..!!")
    else:
        settings.updateData("isProtected", False)
        print(Fore.LIGHTGREEN_EX)
        print("Login Protection Disabled..!!")


def login():
    print(Fore.CYAN)
    print("Enter Username : ")
    username = pyip.inputStr()
    print("Enter Password : ")
    pwd = pyip.inputPassword()
    choice = pyip.inputYesNo("Remember Me?")

    if db_obj.user_exists(username):
        if db_obj.get_password() == encoder.enencoderer(pwd):
            print(Fore.LIGHTGREEN_EX)
            print("Login Successfull..!!")
            logged_user = db_obj.get_user_id()
            if choice == "yes":
                with open("data.key", "w") as f:
                    f.write(db_obj.get_key())
            return username
        else:
            print(Fore.RED)
            print("Incorrect Password..!!")
    else:
        print(Fore.RED)
        print("Username not found..!!")

    return None


def signup():
    print(Fore.CYAN)
    username = pyip.inputStr("Enter Username : ")
    password = pyip.inputPassword("Enter Password : ")
    re_password = pyip.inputPassword("Re-enter Password : ")
    me = pyip.inputYesNo("Remember Me? ")

    if re_password != password:
        print(Fore.RED)
        print("Password Mismatch.!!")
        return None

    if db_obj.user_exists(username):
        print(Fore.RED)
        print("Username is taken.!!")
        return None
    randText = encoder.getRandomString()
    logged_user = db_obj.insert_user(username, password, randText)
    print(Fore.LIGHTGREEN_EX)
    print("SUCCESSFULLY SIGNED UP")

    if me == "yes":
        with open("secret.key", "w") as f:
            f.write(randText)

    return True
