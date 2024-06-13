import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from lib.helpers import create_user, create_expense, list_users, list_expenses, find_user, delete_user, delete_expense

def main():
    while True:
        print("1. Create User")
        print("2. Create Expense")
        print("3. List Users")
        print("4. List Expenses")
        print("5. Find User")
        print("6. Delete User")
        print("7. Delete Expense")
        print("8. Exit")
        
        choice = input("> ")
        
        if choice == "1":
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            create_user(name, email)
        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            create_expense(description, amount, user_id)
        elif choice == "3":
            users = list_users()
            for user in users:
                print(user)
        elif choice == "4":
            expenses = list_expenses()
            for expense in expenses:
                print(expense)
        elif choice == "5":
            user_id = int(input("Enter user ID: "))
            user = find_user(user_id)
            print(user)
        elif choice == "6":
            user_id = int(input("Enter user ID: "))
            delete_user(user_id)
        elif choice == "7":
            expense_id = int(input("Enter expense ID: "))
            delete_expense(expense_id)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
