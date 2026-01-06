with open('d1p1.in') as f:
    expenses = [int(expense) for expense in f.read().split('\n')]
print(expenses)

for i in expenses:
    for j in expenses[1:]:
        if i + j == 2020:
            print(i, j, i+j, sep=", ")
            print(i * j)