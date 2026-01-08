with open('d3p1.in') as f:
    grid = [list(i) for i in f.read().split('\n')]

trees = 0
for i, y in enumerate(grid[1:], 1):
    print(y)
    if y[(i * 3) % len(y)] == '#':
        trees += 1
        print(f'tree at {i*3%len(y)}, {i}')

print(f'{trees = }')