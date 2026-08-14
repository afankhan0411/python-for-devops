# try:
#     number = int("abc")
#     print(number)
# except ValueError:
#     print("Could not convert to number")

# servers = {"web1": 45, "web2": 70, "db1": 90}


     
# try:
#     server_name = "cache1"
#     a = servers[server_name]
#     print(a)
# except KeyError:
#     print("value does not exist")
# finally:
#     print("Lookup attempt finished")    



# import json

# data = [{"name": "web1",  "status": "running", "cpu": 47, "region": "us-east1"}, {"name": "web2",  "status": "running", "cpu": 21, "region": "us-east-2"}]

# with open("config.json", "w") as f:
#     json.dump(data, f)

# with open("config.json", "r") as f:
#     loaded = json.load(f)
#     print(loaded[1]["region"])


# import requests


# try:
#     output = requests.get("https://api.github.com/users/torvalds")
#     data = output.json()
#     print(data["name"])
#     print(data["public_repos"])
#     print(data["followers"])

# except requests.exceptions.RequestException:
#     print("Network Failure")

# import requests
# def check_url(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             result = url + "is up status = " + str(response.status_code)
#         else:
#             result = url + "is down status = " + str(response.status_code)
#     except requests.exceptions.RequestException:
#         result = url + "is unreachable"

#     with open("health_check.log", "a") as f:
#         f.write(result + "\n")           


# urls = ["https://www.google.com", "https://thisisnotarealsite12345.com"]

# for url in urls:
#     check_url(url)


config = {
    "name": "web1",
    "environment": "production",
    "port": 8080,
    "region": "us-east-1"
}

print("port" in config)







