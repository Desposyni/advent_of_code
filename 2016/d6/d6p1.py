from collections import Counter

with open('d6p1.in') as f:
    rows = f.read().split('\n')

columns = list(zip(*rows))
for column in columns:
    print(Counter(column).most_common(1)[0][0], end='')