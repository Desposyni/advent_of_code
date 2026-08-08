with open("d3p1.in") as f:
    directions = f.readline()

print(directions)
houses = set()
x, y = 0, 0
houses.add((x,y))
for d in directions:
    if d == "^":
        y += 1
    elif d == ">":
        x += 1
    elif d == "v":
        y -= 1
    elif d == "<":
        x -= 1
    houses.add((x, y))
print(len(houses))
