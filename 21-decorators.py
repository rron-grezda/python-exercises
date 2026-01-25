def decorator(function):
    def inner_function():
        return function().upper()
    return inner_function

@decorator
def decorated_function():
    return "This is a decorated text"

print(decorated_function())

print("--------------------")

# Multiple decorations
def multiple_decorators(func):
    def decorate():
        return func().upper()
    return decorate

@multiple_decorators
def first_dec_func():
    return "First decorated function."

@multiple_decorators
def sec_dec_func():
    return "Second decorated function."

print(first_dec_func())
print(sec_dec_func())


print("--------------------")


def divide(function):
    def div(x, y):
        if y == 0:
            return "Division by zero is not allowed!"
        return function(x, y)
    return div

@divide
def divide_numbers(x, y):
    return x / y

print(divide_numbers(56, 7))
print(divide_numbers(10, 0))