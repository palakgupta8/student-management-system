import csv

students = []

def add_student():
    
    ids = int(input("\nEnter id: "))
    for student in students:
        if student["id"] == ids:
            print("\nid already exist")
            return
        
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    marks = int(input("Enter marks : "))

    student = {
    "id": ids,
    "name": name,
    "age": age, 
    "marks": marks
    }

    students.append(student)
    print("\nStudent Added Successfully.")


def display_student():

    if len(students) == 0:
        print("\nNo students found.")
        return

    for student in students:
        print("--------------------")
        print("ID :", student["id"])
        print("Name :", student["name"])
        print("Age :", student["age"])
        print("Marks :", student["marks"])
        print("--------------------")


def display_student():

    if len(students) == 0:
        print("\nNo students found.")
        return

    for student in students:
        print("--------------------")
        print("ID :", student["id"])
        print("Name :", student["name"])
        print("Age :", student["age"])
        print("Marks :", student["marks"])
        print("--------------------")



def search_student():

    student_id = int(input("\nenter student id: "))
    for student in students:
        if student["id"]==student_id:
            print("--------------------")
            print("ID :", student["id"])
            print("Name :", student["name"])
            print("Age :", student["age"])
            print("Marks :", student["marks"])
            print("--------------------")
            return

    else:
        print("\nStudent not found.")


def update_student():

    student_id = int(input("\nenter student id: "))
    for student in students:
        if student["id"]==student_id:
            student_name = (input("\nenter student new name: "))
            student_age = int(input("enter student new age: "))
            student_marks = int(input("enter student new marks: "))

            student["name"]=student_name
            student["age"]=student_age
            student["marks"]=student_marks

            print("\nStudent Updated Successfully.")
            print("--------------------")
            print("ID :", student["id"])
            print("Name :", student["name"])
            print("Age :", student["age"])
            print("Marks :", student["marks"])
            print("--------------------")
            return

    else:
        print("\nstudent not found")



def delete_student():
    student_id = int(input("enter student id: "))
    for student in students:
        if student["id"]==student_id:
            students.remove(student)
            print("\nStudent deleted Successfully.")
            return
    else:
        print("\nstudent not found")


def save_to_csv():

    with open("students.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Age", "Marks"])

        for student in students:
            writer.writerow([
                student["id"],
                student["name"],
                student["age"],
                student["marks"]
            ])

    print("Students saved successfully.")
    

def read_from_csv():

    with open("students.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            student = {
                "id": int(row[0]),
                "name": row[1],
                "age": int(row[2]),
                "marks": int(row[3])
            }

            students.append(student)

    print("Students loaded successfully.")
    
