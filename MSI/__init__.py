#!/usr/bin/env python3

from socket import gethostname
from os import system
from datetime import datetime
from rich import print
from psutil import virtual_memory, cpu_count, cpu_freq, cpu_percent, boot_time


class MSI:
    def __init__(self):
        self.cls_terminal = lambda : system('cls' if os_name == 'nt' else 'clear')
        self.username = gethostname()
        self.menu()

    def menu(self):
        ascii = ascii = '''[bold magenta]
                     _
     ____ ___  _____(_)
    / __ `__ \/ ___/ /
   / / / / / (__  ) /
  /_/ /_/ /_/____/_/
[/bold magenta]'''
        print(ascii)
        print(f"[bold white]. . . . . . . . . . . . . . . .[/bold white]\n")
        self.sysinfo()

    def sysinfo(self):
        availableMem = round(virtual_memory().total / (1024.0 ** 3), 2)
        cpuFreq = cpu_freq().current
        cpuCount = cpu_count()
        cpuPercent = cpu_percent()
        bootTime = datetime.fromtimestamp(boot_time()).strftime('%Y-%m-%d %H:%M:%S')
        print_cont = [f"[bold green]#[/bold green] Available memory: {availableMem} GB\n",
                     f"[bold green]#[/bold green] CPU Amount: {cpuCount}\n"
                     f"[bold green]#[/bold green] CPU Frequency: {cpuFreq} MHz\n"
                     f"[bold green]#[/bold green] CPU Usage Percentage: {cpuPercent}\n"
                     f"[bold green]#[/bold green] Boot Time: {bootTime}"]

        for content in print_cont:
            print(content)
