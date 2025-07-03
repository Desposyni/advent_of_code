from collections import namedtuple

target = 361527
stop = 20

Mem_Loc = namedtuple('Mem_Loc', ['x', 'y', 'v'])

memory = [Mem_Loc(0, 0, 1)]
print(memory[-1].x, memory[-1].y)

for i in range(1, stop):
    d = 1 if i % 2 else -1
    for x in range(i):
        # if memory[-1].v == target: break
        memory.append(Mem_Loc(memory[-1].x + d, memory[-1].y, memory[-1].v + 1))
        print(memory[-1].x, memory[-1].y)
    for y in range(i):
        # if memory[-1].v == target: break
        memory.append(Mem_Loc(memory[-1].x, memory[-1].y + d, memory[-1].v + 1))
        print(memory[-1].x, memory[-1].y)

distance = abs(memory[-1].x) + abs(memory[-1].y)
print(distance, 'steps away')

for i, location in enumerate(memory):
    if i == 0: continue
    v = 0
    for previous in memory[:i]:
        if previous.x == location.x - 1 and previous.y == location.y - 1:
            v += previous.v
        elif previous.x == location.x and previous.y == location.y - 1:
            v += previous.v
        elif previous.x == location.x + 1 and previous.y == location.y - 1:
            v += previous.v
        elif previous.x == location.x - 1 and previous.y == location.y:
            v += previous.v
        elif previous.x == location.x + 1 and previous.y == location.y:
            v += previous.v
        elif previous.x == location.x - 1 and previous.y == location.y + 1:
            v += previous.v
        elif previous.x == location.x and previous.y == location.y + 1:
            v += previous.v
        elif previous.x == location.x + 1 and previous.y == location.y + 1:
            v += previous.v

    print(v)
    memory[i] = Mem_Loc(location.x, location.y, v)
    if v > target:
        print(v)
        break