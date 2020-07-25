import socket
import os

from datetime import datetime # Time
from colorama import Fore # Color
from psutil import virtual_memory, cpu_count, cpu_freq, cpu_percent, boot_time # Get system info

ascii = """
                        _ 
        ____ ___  _____(_)
       / __ `__ \/ ___/ / 
      / / / / / (__  ) /  
     /_/ /_/ /_/____/_/ 

 my sistem info 2.0 | oppsec           
"""

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clearTerminal()

    ## BANNER
    print(Fore.YELLOW + ascii)
    print(Fore.WHITE + ". . . . . . . . . . . . . . . . \n")

    username = socket.gethostname()
    print(f'[!] - Welcome {username} \n')

    ## CALL SYSTEM INFO FUNCTION
    sysinfo()

def sysinfo():

    availableMemory = virtual_memory()
    cpuFreq = cpu_freq()
    bootTime = datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    print('[#] Available memory:', availableMemory.available, '\n')

    print('[#] CPU Amount:', cpu_count())
    print('[#] CPU Frequency:', cpuFreq.current)
    print('[#] CPU Use Percentage:', cpu_percent(), '\n')

    print('[#] Boot Time:', bootTime)

menu()
