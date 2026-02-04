'''
In Python, dictionaries (dicts) are a built-in data type used to store data in key-value pairs.
'''
students = {
    # key: value
    "name": "Rron",
    "surname": "Grezda",
    "age": "24"
}

for key, value in students.items():
    print(key + ": " + str(value))

print(students["name"] +" "+ students["surname"] +" "+ str(students["age"]))

print("- - - Dictionary functions - - -")

students.update({"avg_grade": "8.5"})       # Create - adds key, value to the dicts
print(students)

print(students.get("age"))      # Read 

#students.clear()       clears the items in dicts

print(students.keys())          # prints keys
print(students.values())        # prints values



print("--------------------------")
residence = {
    "name": "Rron",
    "surname": "Grezda",
    "city": "Espoo",
    "state": "Finland"
}

print(residence["city"])