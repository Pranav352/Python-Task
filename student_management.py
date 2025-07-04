students = []

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    grades = input("Enter grades separated by commas: ")
    grade_list = [float(g.strip()) for g in grades.split(",")]
    student = {
        "name": name,
        "id": student_id,
        "grades": grade_list
    }
    students.append(student)
    print("Student added successfully.\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    for i, student in enumerate(students):
        avg = sum(student["grades"]) / len(student["grades"])
        print(f"{i + 1}. {student['name']} (ID: {student['id']}) - Grades: {student['grades']} | Average: {avg:.2f}")
    print()

def main():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("👋 Exiting... Goodbye!..")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()




