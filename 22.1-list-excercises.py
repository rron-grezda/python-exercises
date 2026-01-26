# 1.Print 1st and last element of the list
list = [1, 2, 3, 4, 5, 6]

print(list[0])
print(list[-1])

# 2.Print names of the list with for loop
names = ["Rron", "Oliver", "Ajan", "Ryan", "Nora", "Rima"]

for name in names:
    print(name)

# 3.Add an element on the list
names.append("Kumba")
print(names)

# 4.Remove second element from the list
del names[1]
print(names)

# 5.Check if an element is in the list
if "Ajan" in names:
    print("This name is in the list.")
else:
    print("This name is NOT in the list.")