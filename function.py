num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print(f"{num1}+{num2}={add(num1, num2)}")
print(f"{num1}-{num2}={sub(num1, num2)}")
print(f"{num1}x{num2}={mul(num1, num2)}")
print(f"{num1}/{num2}={div(num1, num2)}")


