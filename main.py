expenses = []




def add_expense():
    while True:
        try:
            amount = float(input("Enter your expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero. Try again")
            else:
                break

        except ValueError:
            print("Invalid input. Try again")

    category = input("Enter your expense category: ").title().strip()
    while not category:
        print("Category cannot be empty. Try again.")
        category = input("Enter your expense category: ").title().strip()

    note = input("Enter a short note to add: ").strip()
    while not note:
        print("Note cannot be empty. Try again.")
        note = input("Enter a short note to add: ").strip()

    expense = {"amount": amount, "category": category, "note": note}
    expenses.append(expense)
    print("Expense added successfully!")



def view_expenses():
    if not expenses:
        print("No expenses added")
    else:
        print(" ===YOUR EXPENSES===")
        for index, expense in enumerate(expenses, start=1):
            print(f"\nExpense {index}")
            print(f"Amount: ${expense['amount']:.2f}")
            print(f"Category: {expense['category'].title()}")
            print(f"Note: {expense['note'].title()}")

    print(f"Total expenses added: {len(expenses)}")




def total_expenses():
    total = 0
    if not expenses:
        print("No expenses added")
    else:
        for expense in expenses:
            total += expense["amount"]
        print(f" Total expenses: ${total:.2f}")

def delete_expense():
    if not expenses:
        print("No expenses added")
    else:
        view_expenses()
        while True:
            try:
                number = int(input("Enter the expense number to delete: "))

                if number < 1 or number > len(expenses):
                    print("Invalid input. Try again")
                else:
                    break

            except ValueError:
                print("Invalid input. Try again")


        confirm = input("Are you sure you want to delete the expense? (y/n): ").lower()
        if confirm == "y":
            del expenses[number - 1]
            print(f" Expense {number} has been deleted")
        else:
            print("Deletion cancelled")

def average_expense():
    if not expenses:
        print("No expenses added")
    else:
        total = 0
        for expense in expenses:
            total += expense["amount"]
        count = len(expenses)
        average = total / count
        print(f"Average expense: ${average:.2f}")

def edit_expense():
    if not expenses:
        print("No expenses added")
    else:
        view_expenses()

        while True:
            try:
                number = int(input("which expense would you like to edit? "))
                if number < 1 or number > len(expenses):
                    print("Invalid input. Try again")
                else:
                    break
            except ValueError:
                print("Invalid input. Try again")

        expense = expenses[number - 1]
        edit_type = input("What do you want to edit? (amount/category/note): ").lower().strip()
        if edit_type == "amount":
            while True:
                try:
                    amount = float(input("Enter your new expense amount: "))
                    if amount <= 0:
                        print("Amount must be greater than zero. Try again")
                    else:
                        expense["amount"] = amount
                        break
                except ValueError:
                    print("Invalid input. Try again")



        elif edit_type == "category":
            category = input("Enter your new expense category: ").title().strip()

            while not category:
                print("Category cannot be empty. Try again")
                category = input("Enter your new expense category: ").title().strip()

            expense["category"] = category

        elif edit_type == "note":
            note = input("Enter your new expense note: ").strip()

            while not note:
                print("Note cannot be empty. Try again")
                note = input("Enter your new expense note: ").strip()
            expense["note"] = note

    print("Expense updated successfully!")

def search_expense():
    if not expenses:
        print("No expenses added")
    else:
        expense_category = input("Enter your expense category: ").strip().lower()
        found = False
        for expense in expenses:
            if expense["category"].lower() == expense_category:
                print(expense)
                found = True
        if not found:
            print("No matching expenses found")






print("Welcome to the expense tracker! ")
while True:

    print("1. Add expense")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Delete expense")
    print("5. average expense")
    print("6. Edit expense")
    print("7. Search expense")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 8:
            print("Invalid input. Try again")
            continue

    except ValueError:
        print("Invalid input. Try again")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total_expenses()
    elif choice == 4:
        delete_expense()
    elif choice == 5:
        average_expense()
    elif choice == 6:
        edit_expense()
    elif choice == 7:
        search_expense()
    elif choice == 8:
        print("Thank you for using expense tracker")
        break
    else:
        print("Invalid choice. Try again")






