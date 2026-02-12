'''
Error handling in Python is a way to manage and respond to errors in your program without crashing it.
    try     -code that might cause an error
    except  -code that runs if an error happens
    finally -ALWAYS runs
'''

try:
    print(x)
except:
    print("Error - x is not defined!")
finally:
    print("Finally!")