with open('d5p1.in') as f:
    offsets = f.read().split('\n')
offsets = [int(offset) for offset in offsets]

i = 0
step = 0
while 0 <= i < len(offsets):
    step += 1
    print(step)
    next_i = i + offsets[i]
    offsets[i] += 1
    i = next_i