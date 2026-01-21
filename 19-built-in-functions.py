# len()

word = input("Enter a word: ")
print("The length of this word is:", len(word))


# Get an input from user, then change the type to int() and float()

number_text = input("Enter a number: ")

number_int = int(number_text)
number_float = float(number_text)

print("Integer value:", number_int)
print("Float value:", number_float)


# Find absolute value abs()

number = int(input("Enter a positive or negative number:"))

absolute_value = abs(number)
print(absolute_value)


# type()
int_number = 10
float_number = 3.14
text = "This is a text."

print("Type of the given number is:", type(int_number))
print("Type of the given number is:", type(float_number))
print("Type of the given text is:", type(text))


# Find the highest and lowest number from user. max(), min()

numbers = []

for i in range(5):
    number = int(input("Enter numbers: "))
    numbers.append(number)    # append() - adds numbers to the list.

print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))


# Calculate the total of the numbers given in the list: sum()

numbers = []

for i in range(4):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("The sum of the numbers is: ", sum(numbers))

print("---Same excercise, but values given in the list---")

numbers = [5, 10, 20, 25, 40, 60]

total = sum(numbers)
print(total)


# Sort numbers in the list. sorted()

list = [45, 64,1, 10, 87, 100]

print("Original list:", list)
print("Sorted numbers in the list: ", sorted(list))


# Round the decimal number. round()

number = float(input("Enter a decimal number: "))

print("The rounded number is:", round(number))


# str.lower(), str.upper()

text = input("Write a small text: ")

print("Lowercase text:", str.lower(text))
print("Uppercase text:", str.upper(text))


# count()

sentence = input("Write a sentence: ")
letter = input("Which letter to count: ")

count_letter = sentence.count(letter)
print(f"The letter {letter} appears {count_letter} times in the sentence.")


# range()

for number in range(1, 21):
    if number %2 == 0:
        print(number)

'''
Write a program that:
    -Takes 5 grades from the user
    -Stores them in a list
Prints:
    -The average grade (using sum() and len())
    -The highest grade (max())
    -The lowest grade (min())
'''
grades = []

for i in range(5):
    grade = int(input("Enter grade: "))
    grades.append(grade)

average_grade = sum(grades) / len(grades)
highest_grade = max(grades)
lowest_grade = min(grades)

print("Average grade is: ", average_grade)
print("Highest grade is: ", highest_grade)
print("Lowest grade is: ", lowest_grade)