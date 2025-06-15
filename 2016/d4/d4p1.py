from re import findall, search
from collections import Counter

with open('d4p1.in') as f:
    rooms = f.read().split('\n')

real_rooms = []
for room in rooms:
    name = ''.join(findall(r'([a-z]+)-', room))
    sector = int(search(r'\d+', room).group())
    checksum = search(r'\[(\w{5})', room).group(1)
    name_count = Counter(sorted(name)).most_common(5)
    name_count = dict(name_count)

    if sorted(checksum) == sorted(name_count):
        real_rooms.append(sector)
print(sum(real_rooms))
