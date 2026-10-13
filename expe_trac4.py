# ========== EXPENSE TRACKER ==========

# 1. Add Expense
# 2. View Expenses
# 3. Total Expenses
# 4. Highest Expense
# 5. Lowest Expense
# 6. Exit

# Category: Food
# Description: Lunch
# Amount: 250

# category
# description
# amount
# date
import datetime
exepenses = []

while True:
    choose = int(input("Please choose an option: "))
    if choose == 1:
        Category = input("Please enter Category: ")
        Desc = input("Please enter Description: ")
        amt = int(input("Please enter Amount: "))
        tim = datetime.datetime.now().date()
       

        expense_item = {
        "category": Category,
        "description": Desc,
        "amount": amt,
        "date": tim,
        

    }
        exepenses.append(expense_item)
    if choose == 2:
        if not exepenses:
            print("No any expenses")
        else:
            for i, no in enumerate(exepenses, start=1):
                print(f"Item {i}:  Category {no['category']} Des {no['description']} Amount {no['amount']} Date {no['date']}")