"""
All Basic Functions Needed Here
Creator -> Swarup Deepak Vishwas

Modules To Install
1. colorama
"""

# Imports Here

from colorama import Fore
from sys import exit

from requests import get


# Print Logo
def printBrand(brand, color=Fore.CYAN, symbol="#"):
    print(color)
    print(symbol * (len(brand) + 20))
    print(brand.center(len(brand) + 20))
    print(symbol * (len(brand) + 20))


# Numeric Menu
def myMenu(options, color=Fore.CYAN):
    # print(len(options))
    if len(options) == 0:
        print(Fore.LIGHTRED_EX)
        print("No Options Given..!!")
        exit()
    print(color)
    print()
    print("-" * 30)
    print("YOUR MENU".center(30))
    print("-" * 30)
    print()
    i = 1
    for option in options:
        print(i, ".", option)
        i += 1
    try:
        ch = int(input("Enter your choice : "))
    except ValueError:
        print(Fore.RED)
        print("Enter the Number Mate..!!")
        ch = 0
    # print(ch > len(options))
    if ch > len(options) or ch <= 0:
        print(Fore.RED)
        print("Invalid Option Mate..!!")

    return ch


# Exit Statement
def quitMe():
    print(Fore.GREEN)
    print("#" * 50)
    print("Thanks For Using Our Software".center(50))
    print("#" * 50)
    print()
    print(Fore.WHITE)
    exit()


# About Me
def aboutMe():
    print(Fore.MAGENTA)
    print("=" * 40)
    indic = {
        "name": "Swarup Vishwas",
        "socials": {
            "Instagram": "swarup.vishwas",
            "Github": "SwarupVishwas18",
            "Leetcode": "SwarupVishwas18",
        },
        "description": "Things aren’t always #000000 and #FFFFFF!",
    }
    # print(indic)
    print(f"Name : {indic['name']}")
    for socialApp, socialId in indic["socials"].items():
        print(f"{socialApp} : {socialId}")
    print(indic["description"])
    print("=" * 40)
