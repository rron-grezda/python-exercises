# Find the vowels in the text.
sentence = "Python is an easy and powerful programming language used for many purposes."

counter = 0
for letter in sentence:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        counter+=1

print(counter)