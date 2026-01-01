age = int(input("HI! Please enter your age: \n"))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

score = int(input("HI! Please enter your score: \n"))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("your grade is:", grade)

