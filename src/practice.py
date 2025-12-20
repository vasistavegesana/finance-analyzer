expenses = [
    {"category": "rent", "amount": 2500},
    {"category": "food", "amount": 750},
    {"category": "trip", "amount": 500}
]

first_expense = expenses[0]
print("The cost for the rent is", first_expense["amount"])

total = 0
for item in expenses:
    total = total +item["amount"]
    print(item["category"], item["amount"])

print(total)