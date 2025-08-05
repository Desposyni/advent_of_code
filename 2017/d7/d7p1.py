from re import findall
from collections import Counter

with open('d7p1.in') as f:
    info = f.read()

progs = findall(r'[a-z]+', info)
progs_count = Counter(progs)

for k, v in progs_count.items():
    if v == 1:
        print(k)