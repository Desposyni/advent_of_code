with open("d1p1.in") as f:
    rotations = [(rotation[0], int(rotation[1:])) for rotation in f.read().split("\n")]

dial = 50
password = 0
for direction, distance in rotations:
    if direction == 'R':
        dial += distance
    elif direction == 'L':
        dial -= distance
    dial %= 100
    if dial == 0:
        password += 1
    print(direction, distance, dial, password)
