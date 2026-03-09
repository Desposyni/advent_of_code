with open("d2p1.in") as f:
    commands = f.read().split("\n")

x, y, aim = 0, 0, 0
for command in commands:
    direction, distance = command.split()
    distance = int(distance)
    if direction == "up":
        aim -= distance
    elif direction == "down":
        aim += distance
    else:
        x += distance
        y += aim * distance
print(x * y)
