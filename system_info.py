from psutil import virtual_memory, cpu_count, cpu_freq, cpu_stats, cpu_percent, boot_time
from datetime import datetime
from os import system, name
from colorama import Fore

class system1():
    def __init__(self):
        self.time = datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        self.mem = virtual_memory()
        self.per = cpu_percent(interval=1)
        self.count = cpu_count()
        self.freq = cpu_freq()
        self.stats = cpu_stats()
        self.clear = lambda : system('cls' if name == 'nt' else 'clear')
        self.print_info()
    
    def print_info(self):
        self.clear() 
        print('*******************')
        print('\n---CPU---')
        print(Fore.YELLOW +'CPU %:', self.per)
        print('CPU Frequence:', self.freq.current)
        print('CPU Cores:', self.count)
        print('CPU Stats:', self.stats.ctx_switches)
        print(Fore.RESET + '\n---MEMORY---')
        print(Fore.YELLOW +'Memory %:', self.mem.percent)
        print('Memory Available:', self.mem.available)
        print('Memory Used:', self.mem.used)
        print(Fore.RESET + '\n---BOOT---')
        print(Fore.YELLOW +'Boot Time:', self.time)