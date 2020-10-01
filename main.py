#!/usr/bin/env python3

from socket import gethostname
from os import system
from os import name as os_name

from datetime import datetime
from rich import print
from psutil import virtual_memory, cpu_count, cpu_freq, cpu_percent, boot_time

ascii = '''[bold magenta]
                        _ 
        ____ ___  _____(_)
       / __ `__ \/ ___/ / 
      / / / / / (__  ) /  
     /_/ /_/ /_/____/_/   

- My System Info 2.1 | @oppsec[/bold magenta]'''

def clearTerminal():
  system('cls' if os_name == 'nt' else 'clear')

def menu():
  bar = (f'[bold white]. . . . . . . . . . . . . . . .[/bold white]\n')
  username = gethostname()
  print(ascii)
  print(f'[!] - Welcome [bold magenta]{username}[/bold magenta] :smiley:\n')
  print(bar)
  sysinfo()
  print(bar)

def sysinfo():
  availableMem = round(virtual_memory().total / (1024.0 ** 3), 2)
  cpuFreq = cpu_freq().current
  cpuCount = cpu_count()
  cpuPercent = cpu_percent()
  bootTime = datetime.fromtimestamp(boot_time()).strftime('%Y-%m-%d %H:%M:%S')

  print(f'[bold green]#[/bold green] Available memory: {availableMem} GB\n')
  print(f'[bold green]#[/bold green] CPU Amount: {cpuCount}')
  print(f'[bold green]#[/bold green] CPU Frequency: {cpuFreq}')
  print(f'[bold green]#[/bold green] CPU Usage Percentage: {cpuPercent}\n')
  print(f'[bold green]#[/bold green] Boot Time: {bootTime}\n')

menu()
