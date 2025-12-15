age = int(input("HI! Please enter your age: \n"))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

marks = int(input("HI! Please enter your marks: \n"))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print("your grade is:", grade)

