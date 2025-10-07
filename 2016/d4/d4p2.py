from re import findall, search
from collections import Counter

with open('d4p1.in') as f:
    rooms = f.read().split('\n')

real_rooms = []
for room in rooms:
    letters = ''.join(findall(r'([a-z]+)-', room))
    name = ' '.join(findall(r'([a-z]+)-', room))
    sector = int(search(r'\d+', room).group())
    checksum = search(r'\[(\w{5})', room).group(1)
    name_count = Counter(sorted(letters)).most_common(5)
    name_count = dict(name_count)

    if sorted(checksum) == sorted(name_count):
        real_rooms.append((name, sector))

for name, sector in real_rooms:
    shift = sector % 26
    for letter in name:
        if letter == ' ':
            print(' ', end='')
            continue
        shifted = ord(letter) + shift
        if shifted > 122:
            shifted -= 26
        print(chr(shifted), end='')
    print(' ', sector)

# ctrl+f for north in the results