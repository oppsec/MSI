import psutil, datetime, sys, main

W  = '\033[0m'
O  = '\033[33m'

def system1():

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_info():
        time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        mem = psutil.virtual_memory()
        per = psutil.cpu_percent(interval=1)
        count = psutil.cpu_count()
        freq = psutil.cpu_freq()
        stats = psutil.cpu_stats()

    def print_info():
        clear() 
        print(W+'*******************')
        print(W+'\n---CPU---')
        print(O+'CPU %:', per)
        print(O+'CPU Frequence:', freq.current)
        print(O+'CPU Cores:', count)
        print(O+'CPU Stats:', stats.ctx_switches)
        print(W+'\n---MEMORY---')
        print(O+'Memory %:', mem.percent)
        print(O+'Memory Available:', mem.available)
        print(O+'Memory Used:', mem.used)
        print(W+'\n---BOOT---')
        print(O+'Boot Time:', time)
        
clear()
get_info()
print_info()

if(__name__ == "__main__"):
    system1()
