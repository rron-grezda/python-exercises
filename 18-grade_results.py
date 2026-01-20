#Check if a student has passed the class.

total = 0
count = 0

while count < 5:
    grade = int(input("Grade the exam: "))
    total += grade
    count += 1

average_grade = total / 5

if average_grade >= 60:
        print("The student has passed the class.")
else:
        print("The student has not passed the class.")