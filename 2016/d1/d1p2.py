from re import findall

with open('d1p1.in') as f:
    directions = f.read()

directions = findall(r'(L|R)(\d+)', directions)
directions = [(i, int(j)) for i, j in directions]

print(directions)