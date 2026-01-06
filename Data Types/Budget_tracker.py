def main():
    expenses =[{'name': 'Flour', 'type': 'Grocery', 'amount': 1000},
               {'name': 'Rice', 'type': 'Grocery', 'amount':500}]
    print("Welcome to Budget Tracker")
    print("--------------------------")
    choise = int(input("1. Add Expense\n2. Show Expenses\n3. Total Expense\n4. Average Expense\nEnter Choise: "))
    if choise == 1:
        expense_name = name()
        expense_tpye = type()
        expense_amount = amount()
        results = store(expenses,expense_name, expense_tpye, expense_amount)
        
    elif choise == 2:
        for i, expense in enumerate(expenses):
            items = expense['name']
            print(f"{i+1}) {items}")
        print(f"Total Items: {i+1}")

    elif choise == 3:
        total_expense = 0
        for expense in expenses:
            total_expense += expense["amount"]
        print(total_expense)

    elif choise == 4:
        total_expense = 0
        total_items = 0
        for expense in expenses:
            total_expense += expense["amount"]
            total_items += 1
        average = total_expense/total_items
        print(f"Average Expense: {average}")

    

def name():
    while True:
        expense_name = input("Name of Expense: ")
        try:
            if expense_name != "":
                return expense_name
        except ValueError:
            pass
def type():
        while True:
            expense_type = input("Type of Expense: ")
            try:
                if expense_type != "":
                    return expense_type
            except ValueError:
                pass
def amount():
    while True:
        expense_amount = input("Enter Amount: ")
        try:
            expense_amount = int(expense_amount)
            if not expense_amount < 0:
                return expense_amount
        except ValueError:
            print("Amount Must be Positive Digit")
            pass
def store(expense,expense_name, expense_type, expense_amount):
    expense["name"] = expense_name
    expense["type"] = expense_type
    expense["amount"] = expense_amount
    return expense

def calulate_total(expenses_amount):
    total = 0
    for expense in expenses_amount:
        total += expense["amount"]
    return total

def calulate_average(expenses_amount):
    total = calulate_total(expenses_amount)
    average = total / len(expenses_amount)
    return average

def category_wise_total(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["type"]
        amount = expense["amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return category_totals
    

    

if __name__ == "__main__":
    main()