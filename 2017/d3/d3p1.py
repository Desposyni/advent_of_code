from collections import namedtuple

target = 361527

Mem_Loc = namedtuple('Mem_Loc', ['x', 'y', 'v'])

memory = [Mem_Loc(0, 0, 1)]
print(memory[-1].x, memory[-1].y)

for i in range(1, target):
    d = 1 if i % 2 else -1
    for x in range(i):
        if memory[-1].v == target: break
        memory.append(Mem_Loc(memory[-1].x + d, memory[-1].y, memory[-1].v + 1))
        print(memory[-1].x, memory[-1].y)
    for y in range(i):
        if memory[-1].v == target: break
        memory.append(Mem_Loc(memory[-1].x, memory[-1].y + d, memory[-1].v + 1))
        print(memory[-1].x, memory[-1].y)

distance = abs(memory[-1].x) + abs(memory[-1].y)
print(distance, 'steps away')