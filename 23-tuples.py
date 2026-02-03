'''
Tuples in Python store multiple items in one variable, like lists, but they are ordered and immutable (cannot be changed after creation).
We use them to protect data from being modified, to group related values, and because they are faster and safer than lists when data should stay constant.
'''

seasons = ("Spring", "X", "Summer", "Autumn", "Winter", "X")

print(seasons[1])
#seasons.append("X season")           -Error: 'tuple' object has no attribute 'append'

for s in seasons:
    print(s)

if "Winter" in seasons:
    print("Cold!")
else:
    print("Not so cold!")

if "X season" not in seasons:
    print("Hot!")
else:
    print("Not so hot!")


list = ["one", "two", "three"]

convert_list_to_tuple = tuple(list)
print(type(convert_list_to_tuple))


print(seasons.count("X"))
print(seasons.index("Autumn"))