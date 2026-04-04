from collections import Counter

with open('d2p1.in') as f:
    boxes = f.read().split('\n')

two = 0
three = 0
for box in boxes:
    counter = {k: v for k, v in Counter(box).items() if v in (2, 3)}
    if 2 in counter.values(): two += 1
    if 3 in counter.values(): three += 1

print(f'{two} * {three} = {two * three}')