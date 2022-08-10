# Author : Swarup Deepak Vishwas AKA Half Blood Prince
from colorama import Fore
from funcs import *

def main():
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
        elif(ch==6):
            # Quit
            print(Fore.GREEN)
            print("Thanks For Using Our Software..!!")
            break
        elif(ch==4):
            configMenu()
        elif(ch==5):
            getCurrentReward()
        else:
            print(Fore.RED)
            print("Wrong Choice Try Again.!!")
            # Check Option Again


main()
