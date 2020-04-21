import system_info
import os

W  = '\033[0m'  # normal

def choose_option():

    print(W+'')
    print('[1] - System Info ')
    option = int(input('Select? '))

    if(option == 1):
       system_info.system1()
    elif option != 1):
       print("Select a valid option")

if(__name__ == "__main__"):
    choose_option()

