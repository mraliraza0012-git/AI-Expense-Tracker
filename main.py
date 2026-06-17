expenses = []
while True: 
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")


    expense = {
        "amount" : amount,
        "category" : category
    }

    expenses.append(expense)


    choice = input("Add another expense? yes/no: ")


    if choice == "no":
        break

print("expenses")


print("All expenses:",expenses)
print("Total expenses:",sum(expenses))
print("Highest expense:",max(expenses))
print("Lowest expense:", min(expenses))
print("Average expense:", sum(expenses)/len(expenses))

print("Ai Expense Tracker")
print("This code was added in expense-report branch")
print("Branch Test 2026")
