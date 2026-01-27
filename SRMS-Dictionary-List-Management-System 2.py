

records = [] 

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))
    student = {
        "Roll no": roll,
        "Name": name,
        "Course": course,
        "Marks": marks
    }
    records.append(student)
    print("Student added successfully\n")

def display_students():
    if len(records) == 0:
        print("No records found\n")
    else:
        print("Student Records:")
        for s in records:
            print("Roll:", s["Roll no"], " Name:", s["Name"], " Course:", s["Course"], " Marks:", s["Marks"])
        print()

def search_student():
    roll = input("Enter Roll Number to Search: ")
    found = False
    for s in records:
        if s["Roll no"] == roll:
            print("Record Found - Roll:", s["Roll no"], " Name:", s["Name"], " Course:", s["Course"], " Marks:", s["Marks"])
            found = True
            break
    if not found:
        print("Student not found\n")

def update_student():
    roll = input("Enter Roll Number to Update: ")
    found = False
    for s in records:
        if s["Roll no"] == roll:
            new_marks = int(input("Enter New Marks: "))
            s["Marks"] = new_marks
            print("Marks updated successfully\n")
            found = True
            break
    if not found:
        print("Student not found\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    found = False
    for s in records:
        if s["Roll no"] == roll:
            records.remove(s)
            print("Record deleted successfully\n")
            found = True
            break
    if not found:
        print("Student not found\n")

def sort_students():
    if len(records) == 0:
        print("No records to sort\n")
    else:
        records.sort(key=lambda x: x["Marks"], reverse=True)
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
