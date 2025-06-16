with open('d1p1.in') as f:
    digits = f.read()
# digits = '91212129'

counter = 0
for i, digit in enumerate(digits):
    if digit == digits[i-1]:
        counter += int(digit)

print(counter)