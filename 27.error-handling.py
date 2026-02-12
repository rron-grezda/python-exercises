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

