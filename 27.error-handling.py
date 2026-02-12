'''
Error handling in Python is a way to manage and respond to errors in your program without crashing it.
    try     -code that might cause an error
    except  -code that runs if an error happens
    finally -ALWAYS runs
'''

try:
    print(x)
except:
    print("Error! X is not defined!")
# finally:
#     print("Finally!")

try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You can not divide by zero!")
except ValueError:
    print("Please enter a valid number!")

print("-------------------------------------")

numbers = [10, 20, 30]

try:
    index = int(input("Enter an index (0, 1, 2): "))
    print("The value of the entered index is: ", numbers[index])
except IndexError:
    print("Index does not exist!")
except ValueError:
    print("Please enter a valid number.")

print("-------------------------------------")

fruits = ["apple", "orange", "lemon", "blueberry", "grape"]
print(fruits)
try:
    
    fruit = input("Enter a fruit to remove: ")
    fruits.remove(fruit)
    print("The fruit was removed successfully.")
    print("Updated list: ", fruits)
except ValueError:
    print("This fruit does not exist in the list.")