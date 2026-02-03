seasons = ("Spring", "Summer", "Autumn", "Winter")

print(seasons[1])

for s in seasons:
    print(s)

if "Winter" in seasons:
    print("Cold!")
else:
    print("Not so cold!")

if "X season" in seasons:
    print("Hot!")
else:
    print("Not so hot!")
#seasons.append("X season")           -Error: 'tuple' object has no attribute 'append'