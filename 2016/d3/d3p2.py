from itertools import batched, chain

with open('d3p1.in') as f:
    triangles = f.read().split('\n')

triangles = [triangle.split() for triangle in triangles]
print(triangles)
triangles = [list(map(int, triangle)) for triangle in triangles]
print(triangles)
triangles = list(map(list, list(batched(triangles, 3))))
print(triangles)
triangles = [list(zip(*batch)) for batch in triangles]
print(triangles)
triangles = list(chain(*triangles))
print(triangles)
triangles = list(map(list, triangles))
print(triangles)

valid = 0

for triangle in triangles:
    c = max(triangle)
    triangle.remove(c)
    a, b = triangle
    if a + b > c:
        valid += 1

print(valid)