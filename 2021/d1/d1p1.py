with open("d1p1.in") as f:
    depths = f.read().splitlines()
depths = [int(x) for x in depths]
print(depths)
counter = 0
previous = depths[0]
for depth in depths[1:]:
    if depth > previous:
        counter += 1
    previous = depth
print(counter)