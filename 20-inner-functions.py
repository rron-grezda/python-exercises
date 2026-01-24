def calculator(x, y):

    def add():
        return x + y
    
    def substract():
        return x - y
    
    return add, substract

x = int(input("X: "))
y = int(input("Y: "))

plus , minus = calculator(x, y)

print(plus())
print(minus())