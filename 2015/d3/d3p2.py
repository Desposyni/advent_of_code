with open("d3p1.in") as f:
    directions = f.readline()
houses = set()
x, y, a, b = 0, 0, 0, 0
houses.add((x,y))

for i, d in enumerate(directions):
    if i % 2 == 0:
        if d == "^": y += 1
        elif d == ">": x += 1
        elif d == "v": y -= 1
        elif d == "<": x -= 1
        houses.add((x, y))
    else:
        if d == "^": b += 1
        elif d == ">": a += 1
        elif d == "v": b -= 1
        elif d == "<": a -= 1
        houses.add((a,b))
print(len(houses))
