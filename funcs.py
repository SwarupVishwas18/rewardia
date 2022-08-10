import datetime
from colorama import Fore

def menu():

    print(Fore.CYAN)
    print("#"*20)
    print("Rewardia".center(20, " "))
    print("#"*20)
    print()

    print("1. Add Your Task")
    print("2. View All Of Your Task")
    print("3. Clear All Of Your Task")
    print("4. Configure Reward")
    print("5. View Current Reward")
    print("6. Quit")
    while True:
        try:
            print(Fore.CYAN)
            ch = int(input("Enter Your Choice : "))
        except ValueError:
            print(Fore.LIGHTRED_EX)
            print("Enter Number Mate..!!")
            print()
        else:
            break
    
    return ch

def getScore():
    fs = open('tasks.txt','r')
    lines = fs.readlines()
    fs.close()
    return len(lines)

def checkReward():
    score = getScore()
    print(Fore.LIGHTGREEN_EX)
    print('-'*20)
    if(score%5==0):
        gainSeriesReward()
        print("You have been rewarded with a EPISODE..!!")
    if(score%100==0):
        gainMoviesReward()
        print("BONUS : A Movie..!!")
    print('-'*20)
    

def addTask(task):
    now = datetime.datetime.now()
    st = now.strftime("%d/%b/%Y")
    fs = open('tasks.txt','a+')
    fs.write(st+" "+task+"\n")
    fs.close()
    print(Fore.LIGHTGREEN_EX)
    print('-'*20)
    print("Data Added Successfully..!!")
    print('-'*20)
    score = getScore()
    print("Total Score : ", score)
    checkReward()

def displayTasks():
    fs = open('tasks.txt','r')
    lines = fs.readlines()
    fs.close()
    print(Fore.YELLOW)
    print('-'*20)
    print("Your Total Tasks : ",getScore())
    i = 1
    print('-'*20)
    for line in lines:
        print(i,". ",line)
        i+=1

def clearTasks():
        print(Fore.RED)
        pwd = input("Enter The Password : ")
        if(pwd=="Shinigami"):
            fs = open('tasks.txt','w')
            fs.write('')
            print('-'*20)
            print("All Tasks Deleted Successfully..!!")
            print('-'*20)
            fs.close()
        else:
            print("Didn't Deleted Any Data Cause of Incorrect Password..!!")


def getCurrentReward():
    # TODO : Get Current Reward
    rewardFile = open('rewards.txt','r')
    lines = rewardFile.readlines()
    print(Fore.LIGHTGREEN_EX)
    print(lines[-1])
    rewardFile.close()

def addSeriesReward():
    # TODO : Add Series Here
    name = input("Enter the name of series : ")
    start = int(input("Starting Episode : "))
    end = int(input("Ending Episode : "))
    for i in range(start, end+1):
        addRewardToFile('episodes.txt', f'{name}--{i}')

def addMovieReward():
    # TODO : Add Movie Here
    mov  = input("Enter the name of Movie  : ")
    addRewardToFile('./movies.txt', mov)

def gainSeriesReward():
    # TODO : Gain Reward
    reward = removeFirstLine('episodes.txt')
    reward = "SERIES::"+reward
    rewardFile = open('rewards.txt', 'a+')
    rewardFile.write(reward)
    rewardFile.close()
    print(Fore.LIGHTGREEN_EX)
    print("Reward : " + reward)

def gainMoviesReward():
    # TODO : Gain Reward
    reward = removeFirstLine('./movies.txt')
    reward = "MOVIE::"+reward
    rewardFile = open('rewards.txt', 'a+')
    rewardFile.write(reward)
    rewardFile.close()
    print(Fore.LIGHTGREEN_EX)
    print("Reward : " + reward)


def configMenu():
    print(Fore.CYAN)
    print("1. Add New Movie")
    print("2. Add New Series")
    ch = input("Enter the option : ")

    if ch == '1':
        addMovieReward()
    elif ch == '2':
        addSeriesReward()
    else:
        print(Fore.LIGHTRED_EX)
        print("Enter Above Options Mate")


def removeFirstLine(filename):
    # TODO : Remove First Line
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    # print(lines)
    file = open(filename, 'w')
    ch = lines[0]
    for line in lines:
        if line == lines[0]:
            continue
        else:
            file.write(line)
    file.close()
    return ch


def addRewardToFile(filename, text):
    rewardFile = open(filename, 'a+')
    rewardFile.writelines([text+'\n'])
    rewardFile.close()