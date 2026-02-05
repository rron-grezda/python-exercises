'''
In Python, a STRING is a data type used to store text.
'''
string = (" python is a high-level, interpreted, general-purpose programming language known for its simple, English-like syntax and readability, making it ideal for beginners and rapid development.    ")

for s in string:
    print(s)


print(string[0:16])

# String functions
print(len(string))
print(string.upper())
print(string.lower())
print(string.startswith("P"))
print(string.startswith("p"))
print(string.endswith("development."))
print(string.count("for"))
print(string.split(" "))
print(type(string.split(" ")))
print(string.title())
print(string.capitalize())
print(string.strip()) # Removes spaces at the beginning and at the end
print(string.lstrip()) # Removes spaces at the left
print(string.rstrip()) # Removes spaces at the right