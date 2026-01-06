with open('d1p1.in') as f:
    expenses = [int(expense) for expense in f.read().split('\n')]
print(expenses)

for idx, i in enumerate(expenses):
    for j in expenses[idx:]:
        if i + j == 2020:
            print(i, j, i+j, sep=", ")
            print(i * j)