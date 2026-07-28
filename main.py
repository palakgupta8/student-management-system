from student import add_student
from student import update_student
from student import search_student
from student import delete_student
from student import update_student
from student import save_to_csv
from student import read_from_csv
from student import display_student

while True:

    print("\n1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save to CSV")
    print("7. Read from CSV")
    print("8. Exit")


    choice = int(input("\nEnter your choice : "))
    if choice<=8:
        if choice==1:
            add_student()

        elif choice == 2:
            display_student()

        elif choice==3:
            search_student()

        elif choice==4:
            update_student()

        elif choice==5:
            delete_student()

        elif choice==6:
            save_to_csv()

        elif choice==7:
            read_from_csv()

        elif choice==8:
            print("Exit")
            break

    else:
        print("Invalid choice! \nPlease select between 1 and 8.")
        
    
    