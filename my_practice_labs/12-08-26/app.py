import os
import shutil 
import psutil

usage = shutil.disk_usage("/")

def convert_to_GB():
    total = usage.total / 1024**3
    used = usage.used / 1024**3
    free = usage.free / 1024**3

    print("Disk:", str(round(used)), "GB",  "used of",  str(round(total)), "GB",  str(round(free)), "GB","free")
    
convert_to_GB()    


def list_current_dir():
    current_dir = os.getcwd()
    files = os.listdir(current_dir) 
    print(current_dir)
    print(len(files))

list_current_dir()   

def system_check():
    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU: ", cpu_usage)

    mem_usage = psutil.virtual_memory()
    print("MEM: ", mem_usage.percent)


system_check()    