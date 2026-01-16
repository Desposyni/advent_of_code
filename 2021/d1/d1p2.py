with open("d1p1.in") as f:
    depths = f.read().splitlines()
depths = [int(x) for x in depths]
print(depths)
counter = 0
previous = depths[0] + depths[1] + depths[2]
for i in range(1, len(depths) - 2):
    depth = depths[i] + depths[i + 1] + depths[i + 2]
    if depth > previous:
        counter += 1
    previous = depth
print(counter)