with open('d2p1.in') as f:
    commands = f.read().split('\n')
x, y = 0, 0

for command in commands:
    direction, distance = command.split()
    if direction == 'forward':
        x += int(distance)
    elif direction == 'down':
        y += int(distance)
    else:
        y -= int(distance)
print(x * y)
