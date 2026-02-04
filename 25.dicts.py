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

print("--------------------------")
print(students["name"])
print(students["name"] +" "+ students["surname"] +" "+ str(students["age"]))


residence = {
    "name": "Rron",
    "surname": "Grezda",
    "city": "Espoo",
    "state": "Finland"
}

print(residence["city"])