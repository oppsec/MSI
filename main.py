import socket
import os

from datetime import datetime # Time
from rich import print # CLI Color
from psutil import virtual_memory, cpu_count, cpu_freq, cpu_percent, boot_time # Get system info

ascii = """[bold magenta]
                        _ 
        ____ ___  _____(_)
       / __ `__ \/ ___/ / 
      / / / / / (__  ) /  
     /_/ /_/ /_/____/_/ 

 my sistem info 2.1 | oppsec[/bold magenta]      
"""

dots = "[bold white]. . . . . . . . . . . . . . . .[/bold white] \n"

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clearTerminal()

    ## BANNER
    print(ascii)
    print(dots)

    username = socket.gethostname()
    print(f"[!] - Welcome [bold magenta]{username}[/bold magenta]", ":smiley:", "\n")

    ## CALL SYSTEM INFO FUNCTION
    sysinfo()

def sysinfo():

    availableMemory = virtual_memory()
    cpuFreq = cpu_freq()
    bootTime = datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    print('[bold green]#[/bold green] Available memory:', availableMemory.available, '\n')

    print('[bold green]#[/bold green] CPU Amount:', cpu_count())
    print('[bold green]#[/bold green] CPU Frequency:', cpuFreq.current)
    print('[bold green]#[/bold green] CPU Use Percentage:', cpu_percent(), '\n')

    print('[bold green]#[/bold green] Boot Time:', bootTime, '\n')

    print(dots)

menu()
