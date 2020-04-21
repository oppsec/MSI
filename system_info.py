import psutil, datetime
import sys
import main
import 

W  = '\033[0m'  # normal
O  = '\033[33m' # orange

def system1():

    def get_info():
        time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        mem = psutil.virtual_memory()
        per = psutil.cpu_percent(interval=1)
        count = psutil.cpu_count()
        freq = psutil.cpu_freq()
        stats = psutil.cpu_stats()

    def print_info():
        os.system("cls") 
        print(W+'---mysysinfo---')
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

get_info()
print_info()

if(__name__ == "__main__"):
    system1()
