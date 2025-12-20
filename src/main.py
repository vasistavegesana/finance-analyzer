import csv

print("Finance Analyzer started")

app_name = "Finance Analyzer"
user_name = "Vasista"

print(app_name)
print(user_name)

monthly_income = 5000

def calculate_remaining_money(income, expenses):
    remaining_money = income - expenses
    return remaining_money


def expense_reader():
    with open('data/expenses.csv', "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        # need to define total expense here because
        # python doesnt know what the total expesne value is to start with when it
        # is trying to add values for total expense
        # make sure to put total expense inside function but outside the loop so the value doesnt reset to 0. 

        category_total = {}
        total_expense = 0
        for row in csvreader:
            category = row["category"]
            amount = row["amount"]
            amount = amount.strip(" ")
            
            if amount == "":
                continue
            if category not in category_total:
                category_total[category] = 0
            category_total[category] = category_total[category] + int(amount)
            total_expense = total_expense + int(amount)
        print(category_total)
    return total_expense


total_expense = expense_reader()
remaining_money = calculate_remaining_money(monthly_income, total_expense)

def print_summary(monthly_income, total_expense, remaining_money):
    print("Monthly Income:", monthly_income)
    print("Total Expenses:", total_expense)
    print("Remaining Money:", remaining_money)


print_summary(monthly_income,total_expense,remaining_money)