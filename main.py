expenses = []




def add_expense():
    while True:
        try:
            amount = float(input("Enter your expense amount: "))

            if amount < 0:
                print("Amount cannot be negative. Try again")
            else:
                break

        except ValueError:
            print("Invalid input. Try again")


    category = input("Enter category to add: ").lower()
    note = input("Enter a short note to add: ")
    expense = {"amount": amount, "category": category, "note": note}
    expenses.append(expense)



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



print("Welcome to the expense tracker! ")
while True:

    print("1. Add expense")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Delete expense")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 5:
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
        print("Thank you for using expense tracker")
        break
    else:
        print("Invalid choice. Try again")






