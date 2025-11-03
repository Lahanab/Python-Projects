import datetime


def add_expense(memory):
    desc = input("What did you spend on? ")

    while True:
        amount_input = input("How much did you spend? ")

        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Please enter a valid number (e.g., 12.50).")

    category = input("What Kind of expense? ")
    today = datetime.date.today()

    expense = {"Description" : desc,
               "Amount" : amount,
               "Category" : category,
               "Date" : today
               }
    memory.append(expense)
    print("The expense has been added to the memory.")



def view_expense(memory):
    if len(memory) == 0:
        print("No expenses recorded yet")
        return
    else:
        for index, expense in enumerate(memory, 1):
            print(f'Expense {index}')
            print(f'Description: {expense["Description"]}')
            print(f'Amount: ${expense["Amount"]: .2f}')
            print(f'Category: {expense["Category"]}')
            print(f'Date: {expense["Date"]}')
            print("---------------------------------")

    x = len(memory)

    print("Total expenses: ", x)

def delete_expense(memory):
    view_expense(memory)

    while True:

        delete = input("Enter the number of the expense you want to delete: ")

        try:
            delete = int(delete)

            if 1<= delete <= len(memory):
                del memory[delete -1]
            break
        except ValueError:
            print("Please enter a valid number (e.g., 1, 2).")

    print(f"The expense {delete} has been deleted from the memory.")






memory = []

while True:
    print("1.Add Expense: ")
    print("2.View Expense: ")
    print("3.Delete Expense: ")
    print("4.Quit: ")
    user = input("Choose an option (1, 2, 3, or 4): ")
    if user == "1":
       add_expense(memory)
    elif user == "2":
        view_expense(memory)
    elif user == "3":
        delete_expense(memory)
    elif user == "4":
        print("Good Bye!!!")
        break
    else:
        print("Invalid option")



