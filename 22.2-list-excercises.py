# 1.Calculate the sum and the average of all numbers in the given list.
numbers = [10, 20, 30, 10, 153, 40, 10, 50, 60]

total = sum(numbers)
average = total / len(numbers)

print(total)
print(average)

# 2.Find Min and Max number in the list
print(min(numbers))
print(max(numbers))

# 3.Count how many times a value appears in the list.
print(numbers.count(10))

# 4.Create a new list that contains only the even numbers from the original list.
number_list = [1, 2, 3, 4, 5, 6]
even_numbers = []

for n in number_list:
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers)

# 5.Ask the user to fill the list with numbers.
list_of_numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    list_of_numbers.append(num)

print(list_of_numbers)


positive_numbers = []

for i in list_of_numbers:
    if i >= 0:
        positive_numbers.append(i)

print(positive_numbers)