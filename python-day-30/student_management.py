students = []

# Add 3 Students
for i in range(3):
    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    mark = float(input("Enter student mark: "))

    # Result
    if mark >= 50:
        result = "Pass"
    else:
        result = "Fail"

    # Grade
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "D"

    student = {
        "name": name,
        "age": age,
        "mark": mark,
        "result": result,
        "grade": grade
    }

    students.append(student)


# Display All Students
print("\n========== All Students ==========")

for student in students:
    print("\nName:", student["name"])
    print("Age:", student["age"])
    print("Mark:", student["mark"])
    print("Result:", student["result"])
    print("Grade:", student["grade"])


# Search Student
search_name = input("\nEnter student name to search: ")

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("\n========== Student Found ==========")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Mark:", student["mark"])
        print("Result:", student["result"])
        print("Grade:", student["grade"])

        found = True
        break

if not found:
    print("\nStudent not found.")