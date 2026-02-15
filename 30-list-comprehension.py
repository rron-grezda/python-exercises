'''
List comprehensions in Python are a concise way to create new lists from existing iterables (like lists, tuples, or strings).They allow you to write a for loop (and optional conditions) in a single line of code.
'''

'''
numbers = []

for n in range(1, 21):
    print(n)

for n in numbers:
    if n % 6 == 0:
        print(n)     ⬇️ This code can be written in one line using list comprehension.
'''

numbers = [n for n in range(1, 21)]

new_list = [n for n in numbers if n % 6 == 0]

print(new_list)

# Create a list with the squares of numbers from 1 to 10.
square = [n**2 for n in range(1, 11)]
print(square)

# From the list: ⬇️ create a new list where each number is multiplied by 2.

list_numbers = [5, 8, 12, 3, 7]

multiply_list = [n*2 for n in list_numbers]
print(multiply_list)

# From the list: ⬇️ create a list with only odd numbers.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = [n for n in list if n % 2 != 0]
print(odd_numbers)

# Create a list with words that have more than 4 letters.

fruits = ["apple", "banana", "kiwi", "pear", "watermelon"]

fruit_length = [fruit for fruit in fruits if len(fruit) > 4]
print(fruit_length)