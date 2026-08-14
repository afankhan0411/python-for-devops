server = {"name": "web1", "status": "running", "cpu": 45}


print(server["status"])

server["cpu"] = 50
print(server["cpu"])
print(server)

server["region"] = "us-east"

print(server)

servers = {
    "name": "web1",
    "status": "running",
    "specs": {
        "cpu": 4,
        "ram": 16
    }
}

print(server["name"]["specs"]["cpu"])