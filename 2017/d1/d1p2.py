with open('d1p1.in') as f:
    digits = f.read()

counter = 0
other_side = len(digits) // 2
for i, digit in enumerate(digits):
    if digit == digits[i - other_side]:
        counter += int(digit)

print(counter)
