# 

# import os

# files = os.listdir("logs")


# for file in files:
#     with open("logs/" + file, "r") as f:
#         output = f.read()
#         print(file, "\n" ,output)
        
        # if file == "app1.log":
        #     print(file, "\n", output)
        # elif file == "app2.log":
        #     print(file, "\n", output)
        # elif file == "app3.log":
        #     print(file, "\n", output)    


# def check_servers():
#         with open("activity.log", "a") as f:
#                 output = f.write("Checked Servers - all good\n")
#                 return output


# result = check_servers()
# print(result)           


# def system_check():
#         with open("system.log", "r") as f:
#                 for file in f:
#                         x = file.split()
#                         print(x[1], x[2])
                        

# system_check()



# def read_log(filename):
        
#         try:
#               with open(filename, "r") as f:
#                 print(f.read())
#         except FileNotFoundError:
#                print("file not found!")
               
# result = read_log("system.log")               





import os

files = ["system.log", "servers.csv", "ghost.log"]

for file in files:

        if os.path.exists(file):
                print(file, "file exists")
        else:
                print(file, "file doesnt exists")  




