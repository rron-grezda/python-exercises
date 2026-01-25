students = ["Rron", "John", "Arthur", "Oscar", "Romeo"]
#             0        1        2        3        4
#             0                                  n-1 

print(students[2])
print(students[1:3])

print("--------------------")

#Iterate through elements using a for loop
for student in students:
    print("I am " + student)

print("--------------------")

#Iterate through elements using a while loop
i=0
while(i < len(students)):
    print(students[i])
    i+=1

print("--------------------")

#Check if an element is in the list:  in / not in
if "Oscar" in students:
    print("Oscar is in the list")

if "Nora" not in students:
    print("Nora is NOT in the list")
else:
    print("Nora is in the list")

print("--------------------")

#join()
string_students = ", ".join(students)
print(string_students)

print("--------------------")

#append()
students.append("Nora")
print(students)

print("--------------------")

#insert()
students.insert(3, "XYZ")
print(students)

print("--------------------")

#pop()
students.pop(3)
print(students)

print("--------------------")

#remove()
students.remove("Nora")
print(students)

print("--------------------")

#sort()
students.sort() #    0         1        2        3       4
print(students) # ["Arthur", "John", "Oscar", "Romeo", "Rron"]

print("--------------------")

#reverse()
students.reverse()  #   0        1        2        3       4
print(students)     #['Rron', 'Romeo', 'Oscar', 'John', 'Arthur']

print("--------------------")

#Change the value of an element
students[2] = "Nora" # The value at index [2] – Oscar is changed to ‘Nora’.
print(students) # ['Rron', 'Romeo', 'Nora', 'John', 'Arthur']