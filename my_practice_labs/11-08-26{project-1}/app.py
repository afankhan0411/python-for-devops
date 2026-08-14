import os

def error_count(folders):
    try:
        files = os.listdir(folders)
    except FileNotFoundError:
        print("file not found")
        return
    for file in files:
        count = 0
        with open(folders + file, "r") as f:
            for line in f:
                x = line.split()
                if "ERROR" in x: 
                    count += 1
        print(file, count)
        with open("report.log", "a") as f:
            f.write(str(file) + " " + str(count) + " " + "errors\n")
            
                            

error_count("logs/")                 

                            

