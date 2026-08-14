counter = 0


with open("app.log", "r") as f:
    content = f.readlines()

    for linenumber, line in enumerate(content, start=1):
        if "ERROR" in line:
            counter += 1
            print("line" + " " + str(linenumber) + ": " + line) 
    print("Total_Error: ", counter)