expenses = []




def add_expense():

    amount = float(input("Enter amount to add: "))
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
        number = int(input("Enter the expense number to delete: "))
        if number >= 1 and number <= len(expenses):
            del expenses[number - 1]
            print(f" Expense {number} has been deleted")
        else:
            print("Invalid choice. Try again")







print("Welcome to the expense tracker! ")
while True:

    print("1. Add expense")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Delete expense")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
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






