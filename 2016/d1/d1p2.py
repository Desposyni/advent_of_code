from re import findall

with open('d1p1.in') as f:
    instructions = f.read()
# makes a list of coupled directions and distances
instructions = findall(r'([LR])(\d+)', instructions)
# converts numerical strings into integers within the list
instructions = [(i, int(j)) for i, j in instructions]

print(instructions)

# headings are multipliers for effecting direction
# headings = {'N': 1, 'W': 1, 'S': -1, 'E': -1}
# directions are multipliers for effecting direction
# directions = {'L': -1, 'R': 1}
# heading tracks the current direction we're looking
heading = 'N'
# places tracks the places we've visited in (x, y) format
places = [(0, 0)]

for direction, distance in instructions:

    if heading == 'N':
        heading = 'E' if direction == 'R' else 'W'

    elif heading == 'W':
        heading = 'N' if direction == 'R' else 'S'

    elif heading == 'S':
        heading = 'W' if direction == 'R' else 'E'

    elif heading == 'E':
        heading = 'S' if direction == 'R' else 'N'

    for _ in range(distance):
        x, y = places[-1]
        if heading == 'N':
            places.append((x, y + 1))
        elif heading == 'W':
            places.append((x - 1, y))
        elif heading == 'S':
            places.append((x, y - 1))
        elif heading == 'E':
            places.append((x + 1, y))
        print(places)
        if places.count(places[-1]) > 1:
            print(places[-1])
            print(abs(places[-1][0]) + abs(places[-1][1]), 'blocks away')
            print(f'You were here at step {places.index(places[-1])}')
            exit()