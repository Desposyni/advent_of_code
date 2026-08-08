with open('d2p1.in') as f:
    boxes = f.read().split("\n")
total_paper = 0
for box in boxes:
    dimensions = box.split('x')
    x = int(dimensions[0])
    y = int(dimensions[1])
    z = int(dimensions[2])

    minValue = min(x*y, x*z, y*z)
    total_paper += 2*x*y + 2*x*z + 2*y*z + minValue
print(total_paper)