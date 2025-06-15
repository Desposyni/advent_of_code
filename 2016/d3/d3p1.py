with open('d3p1.in') as f:
    triangles = f.read().split('\n')

triangles = [triangle.split() for triangle in triangles]
triangles = [list(map(int, triangle)) for triangle in triangles]
valid = 0
for triangle in triangles:
    c = max(triangle)
    triangle.remove(c)
    a, b = triangle
    if a + b > c:
        valid += 1

print(valid)