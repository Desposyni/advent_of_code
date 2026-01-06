with open('d1p1.in') as f:
    expenses = [int(expense) for expense in f.read().split('\n')]
print(expenses)

for idx, i in enumerate(expenses):
    for jdx, j in enumerate(expenses[idx:-1]):
        for k in expenses[jdx:]:
            if i + j + k == 2020:
                print(i, j, k, i+j+k, sep=", ")
                print(i * j * k)