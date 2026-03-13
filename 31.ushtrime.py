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


num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

largest = num1

if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

print("The largest number is: ", largest)