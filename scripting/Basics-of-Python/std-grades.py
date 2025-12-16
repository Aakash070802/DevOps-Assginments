students = {}

while True:
    print("\n1. Add / Update Student")
    print("2. View All Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")

        if name in students:
            students[name] = grade
            print("Grade updated successfully.")
        else:
            students[name] = grade
            print("Student added successfully.")
    elif choice == '2':
        if not students:
            print("No students found.")
        else:
            for name, grade in students.items():
                print(name, ":", grade)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")