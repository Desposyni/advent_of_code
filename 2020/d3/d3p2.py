with open('d3p1.in') as f:
    grid = [list(i) for i in f.read().split('\n')]
def grid_count(right, down = 1):
    trees = 0
    for i, y in enumerate(grid[down::down], 1):
        if y[(i * right) % len(y)] == '#':
            trees += 1

    print(f'{trees = }')
    return trees

print(grid_count(1) * grid_count(3) * grid_count(5) * grid_count(7) * grid_count(1, 2))