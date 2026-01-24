def decorator(function):
    def inner_function():
        return function().upper()
    return inner_function

@decorator
def decorated_function():
    return "This is a decorated text"

print(decorated_function())