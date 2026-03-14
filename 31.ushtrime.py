# name = input("What is your name? ")
# print("Hello",name,"welcome!")


# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))

# result = num1 + num2
# print("The result is: ", result)


# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("The numebr you entered is EVEN.")
# else:
#     print("The number you entered is ODD.")


# for number in range(1, 11):
#     print(number)


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = int(input("Enter another number: "))

# largest = num1

# if num2 > largest:
#     largest = num2

# if num3 > largest:
#     largest = num3

# print("The largest number is: ", largest)


# word = input("Write a word: ")
# print("The word you entered has", len(word), "letters.")


# for even_number in range(1,21):
#     if even_number % 2 == 0:
#         print(even_number)


# birth_year = int(input("What year were you born: "))
# age = 2026 - birth_year

# print("You are", age, "years old.")


# name = input("Write your name: ")
# print(name.upper())


# birth_year = int(input("Write your birth year: "))
# age = 2026 - birth_year

# if age in range(0, 18):
#     print("You are a minor.")
# elif age in range(18, 65):
#     print("You are mature.")
# else:
#     print("You are old.")


# word = input("Write a word, I will calculate the length: ")

# if len(word) < 5:
#     print("The length of the word is short.")
# elif 5 <= len(word) <= 8:
#     print("The length of the word is average.")
# else:
#     print("The length of the word is long.")


password = input("Type your password: ")

if len(password) < 8 :
    print("Password must be at least 8 characters!")
else:
    print("Password is valid!")