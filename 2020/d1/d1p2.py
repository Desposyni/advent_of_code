with open('d1p1.in') as f:
    expenses = [int(expense) for expense in f.read().split('\n')]
print(expenses)

for i in expenses:
    for j in expenses[1:]:
        for k in expenses[2:]:
            if i + j + k == 2020:
                print(i, j, k, i+j+k, sep=", ")
                print(i * j * k)