with open("d1p1.in") as f:
    rotations = [(rotation[0], int(rotation[1:])) for rotation in f.read().split("\n")]

dial = 50
print(dial)
password = 0
for direction, distance in rotations:
    if direction == 'R':
        password += (dial + distance) // 100
        dial += distance
        dial %= 100

    elif direction == 'L':
        password += abs((dial - distance) // 100)
        if dial == 0: password -= 1
        dial -= distance
        dial %= 100
        if dial == 0: password += 1

    print(direction, distance, dial, password)