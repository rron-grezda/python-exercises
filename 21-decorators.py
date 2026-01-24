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