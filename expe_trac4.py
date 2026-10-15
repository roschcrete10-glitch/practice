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
    try:
        print("#" * 90) 

        
        print("""1. Add Expense
2. View Expenses
3. Total Expenses
4. Highest Expense
5. Lowest Expense
6. Exit""")
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
                    print(f"Item {i}: \n (Category - {no['category']}) \n (Description - {no['description']}) \n (Amount -{no['amount']} Rs.) \n (Date - {no['date']})")

        if choose == 3:
            if not exepenses:
                        print("No any expenses")
            else:
                tot_ex = 0
                amt = 0
                items = []
                for i, no in enumerate(exepenses, start=1):
                    amt += no['amount']
                    tot_ex += 1
                    items.append(no['category'])
                    
                print(f" Total Amount {amt}")
                print(f" Total Expenses {tot_ex} {items}") 

        if choose == 4:
                if not exepenses:
                 print("No any expenses")
                else:
                    highest = max(exepenses, key=lambda x: x['amount'])
                    print(f"\n--- Highest Expense Details ---")
                    print(f"Amount:      {highest['amount']} Rs.")
                    print(f"Description: {highest['description']}")  # <--- Here is your description!
                    print(f"Category:    {highest['category']}")
                    print(f"Date:        {highest['date']}")

        if choose == 5:
            if not exepenses:
                print("No any expenses")
            else:
                    lowest = min(exepenses, key=lambda x: x['amount'])
                    print(f"\n--- Lowest Expense Details ---")
                    print(f"Amount:      {lowest['amount']} Rs.")
                    print(f"Description: {lowest['description']}")  # <--- Here is your description!
                    print(f"Category:    {lowest['category']}")
                    print(f"Date:        {lowest['date']}")

        if choose == 6:
             print("Thanks for choosing us.\nPlease visit again.! Bye")
             break
                         

    except ValueError:
         print("Please enter Valid Input")