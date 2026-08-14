import sys

def add(num1, num2):
    a = num1 + num2
    return a


def sub(num1, num2):
    s = num1 - num2
    return s


num1 = int(sys.argv[1])    
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    result = add(num1, num2)
    print(result)
elif operation == "sub":
    result = sub(num1, num2)

print(result)