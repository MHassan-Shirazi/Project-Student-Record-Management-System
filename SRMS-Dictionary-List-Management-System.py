
students = []   

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    subject = input("Enter Subject: ")
    marks = int(input("Enter Marks: "))
    student = [roll, name, subject, marks]
    students.append(student)
    print("Student added successfully\n")

def display_students():
    if len(students) == 0:
        print("No records found\n")
    else:
        print("Student Records:")
        for s in students:
            print("Roll:", s[0], " Name:", s[1], " Subject:", s[2], " Marks:", s[3])
        print()

def search_student():
    roll = input("Enter Roll Number to Search: ")
    found = False
    for s in students:
        if s[0] == roll:
            print("Record Found - Roll:", s[0], " Name:", s[1], " Subject:", s[2], " Marks:", s[3])
            found = True
            break
    if not found:
        print("Student not found\n")

def update_student():
    roll = input("Enter Roll Number to Update: ")
    found = False
    for s in students:
        if s[0] == roll:
            new_marks = int(input("Enter New Marks: "))
            s[3] = new_marks
            print("Marks updated successfully\n")
            found = True
            break
    if not found:
        print("Student not found\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    found = False
    for s in students:
        if s[0] == roll:
            students.remove(s)
            print("Record deleted successfully\n")
            found = True
            break
    if not found:
        print("Student not found\n")

def sort_students():
    if len(students) == 0:
        print("No records to sort\n")
    else:
        students.sort(key=lambda x: x[3], reverse=True)
        print("Records sorted by marks (high to low)")
        display_students()   

while True:
    print("====== Student Records Management System ======")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Sort Records by Marks")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        sort_students()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again\n")
