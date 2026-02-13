'''
Modules in Python are separate files that contain functions, variables, or classes which can be reused in other programs. They help organize code into smaller, manageable parts instead of writing everything in one file. Modules are used to improve code readability, reusability, and maintainability.
'''

'''
import math_operations as m

print(m.plus(25, 15))
print(m.minus(30, 14))
'''
from math_operations import plus, minus

print(plus(25, 15))
print(minus(30, 14))