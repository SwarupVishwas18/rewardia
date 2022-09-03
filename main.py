# Author : Swarup Deepak Vishwas AKA Half Blood Prince
from colorama import Fore
from funcs import *
import normal
import logging
from datetime import datetime
import settingsData as settings
from time import sleep

logging.basicConfig(filename="log.txt",filemode='w', level=logging.DEBUG,
                    format="%(asctime)s %(message)s")

def main():
    print(Fore.MAGENTA)
    hr = datetime.now().hour
    
    if hr < 12:
        greet = "Good Morning"
    elif hr < 16:
        greet = "Good Afternoon"
    elif hr<22:
        greet = "Good Evening"
    else:
        greet = "Good Night"

    name = settings.getData('Name')

    print(f'{greet} {name}....')
    sleep(3)
    if isProtected():
        login()
    while True:
        

        ch = menu()

        if(ch==1):
            # Add Task
            task = input("Enter Your Task : ")
            addTask(task)
        elif(ch==2):
            # View All Tasks Performed
            displayTasks()
        elif(ch==3):
            # Clear all Tasks
            clearTasks()
        elif(ch==7):
            # Quit
            normal.quitMe()
            break
        elif ch==6:
            normal.aboutMe()
        elif(ch==4):
            configMenu()
        elif(ch==5):
            getCurrentReward()
        else:
            print(Fore.RED)
            print("Wrong Choice Try Again.!!")
            # Check Option Again

try:
    main()
except KeyboardInterrupt:
    normal.quitMe()
except Exception as e:
    print(Fore.RED)
    print("Something has been Wrong, Logging it to logs.txt")
    logging.critical("Program has been Crashed via -> " + str(e).upper())
    normal.quitMe()