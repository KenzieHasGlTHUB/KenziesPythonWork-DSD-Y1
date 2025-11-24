# CRUD Project (Not Finished)
loans = []  

def find_loan_by_id(loan_id):
    """Return a loan dictionary matching loan_id."""
    for loan in loans:
        if loan["loan_id"] == loan_id:
            return loan
    return None


def loan_id_exists(loan_id):
    """Check if loan_id already exists."""
    return any(loan["loan_id"] == loan_id for loan in loans)

def create_loan():
    print("Create New Loan")

    try:
        loan_id = int(input("Enter loan ID (number): "))
    except ValueError:
        print("Loan ID must be a number.")
        return

    if loan_id_exists(loan_id):
        print("Loan ID already exists. Try again.")
        return

    student_name = input("Student name: ")
    student_id = input("Student ID: ")
    device_type = input("Device type (Laptop/Tablet): ")
    device_id = input("Device ID: ")
    date_out = input("Date borrowed (YYYY-MM-DD): ")
    due_back = input("Due back date (YYYY-MM-DD): ")

    loan = {
        "loan_id": loan_id,
        "student_name": student_name,
        "student_id": student_id,
        "device_type": device_type,
        "device_id": device_id,
        "date_out": date_out,
        "due_back": due_back,
        "returned": False
    }

    loans.append(loan)
    print("Loan added successfully!")

def view_all_loans():
    print("All Loan Records")
    if not loans:
        print("No loans found.")
        return

    for loan in loans:
        print(loan)


def search_loans():
    print("Search Loans")
    choice = input("Search by (1) student_id or (2) device_id: ")

    if choice == "1":
        sid = input("Enter student ID: ")
        results = [loan for loan in loans if loan["student_id"] == sid]

    elif choice == "2":
        did = input("Enter device ID: ")
        results = [loan for loan in loans if loan["device_id"] == did]

    else:
        print("Invalid choice")
        return

    if not results:
        print("No matching loans found.")
    else:
        for loan in results:
            print(loan)


def update_loan():
    print("\n--- Update Loan ---")
    try:
        loan_id = int(input("Enter loan ID to update: "))
    except ValueError:
        print("Must be a number.")
        return

    loan = find_loan_by_id(loan_id)

   
 def main_menu():
    while True:
        print("DEVICE LOAN MANAGEMENT SYSTEM")
    
        print("1. Add new loan")
        print("2. View all loans")
        print("3. Search loans")
        print("4. Update loan")
        print("5. Delete loan")
        print("6. Summary")
        print("7. Exit")

        option = input("Choose an option (1-7): ")

        if option == "1":
            create_loan()
        elif option == "2":
            view_all_loans()
        elif option == "3":
            search_loans()
        else:
            print("Invalid Option. Try Again")


if __name__ == "Main"
    main_menu()