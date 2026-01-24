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


def parent():
    def child1():
        return "I am child 1"
    
    def child2():
        return "I am child 2"
    
    return child1, child2

ch1, ch2 = parent()

print(ch1())
print(ch2())