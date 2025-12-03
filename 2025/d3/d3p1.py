with open('d3p1.in') as f:
    banks = [[int(battery) for battery in list(bank)] for bank in f.read().split('\n')]

total_jolts = []

for bank in banks:
    left, right, left_middle, middle_right = 0, 0, 0, 0
    middle = max(bank)
    i = bank.index(middle)
    if i:
        left = max(bank[:i])
    if bank[i+1:]:
        right = max(bank[i+1:])
    if left:
        left_middle = left * 10 + middle
    if right:
        middle_right = middle * 10 + right

    total_jolts.append(max(left_middle, middle_right))

print(sum(total_jolts))