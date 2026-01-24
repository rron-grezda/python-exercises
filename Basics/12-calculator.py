#Functions of the operations
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y!=0:
        return x / y
    else:
        return "You can not divide by 0!"

#Choose the operation
print("Choose an operation: ")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

choose = input("Choose an operation between 1-4: ")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

#Calculate the result
if choose == '1':
    print("Result: ",add(num1, num2))
elif choose == '2':
    print("Result: ", sub(num1, num2))
elif choose == '3':
    print("Result: ", multiply(num1, num2))
elif choose == '4':
    print("Result: ", divide(num1, num2))
else:
    print("Invalid operation, choose an operation between 1-4!")