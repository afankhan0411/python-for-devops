# name = "afan"
# job_title = "devops engineer"
# experience = 3

# print(name + " " + "is a" +  " " + job_title + " "  + "with" + " " + str(experience) + " " + "years of experience")

# cpu_usage = 85

# if cpu_usage >= 90:
#     print("Critical: CPU usage very high")
# elif cpu_usage >= 70:
#     print("Warning: CPU usage high")    
# else:
#     print("Normal: CPU usage healthy")

# servers = ["db3", "web1", "web2", "db1", "cache1"]

# for server in servers:
#     if "db" in server:
#         print("Database server found: " + server)
#     else:
#         print("Regular server: " + server)    

# servers = ["db3", "web1", "web2", "db1", "cache1"]


# def check_server(server):
#     if "db" in server:
#         print("Database is found: " + server)
#     else:
#         print("regular servers " + server)    


# for server in servers:
#     check_server(server)    


server = {"name": "web1", "status": "running", "cpu": 45}

server["status"] = "stopped"
print(server["status"], server["cpu"])

for key, value in server.items():
    print(key, "is", value)

# with open("app.log", "w") as f:
#     f.write("web1\n" "web2\n" "db1\n")

# with open("app.log", "r") as f:
#     content = f.read()
#     print(content)