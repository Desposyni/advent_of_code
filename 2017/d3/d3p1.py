from collections import namedtuple

target = 361527

target = 12

Mem_Loc = namedtuple('Mem_Loc', ['x', 'y', 'v'])

memory = [Mem_Loc(0, 0, 1)]
for i in range(1, target + 1):


'''
 0, 0
 1, 0  
 1, 1
 0, 1 -1, 1
-1, 0 -1,-1
 0,-1  1,-1  2,-1
 2, 0  2, 1  2, 2
 1, 2  0, 2 -1, 2 -2, 2
 

while v < target
    x + i
        v += i
    y + i
        v += i
    i++
    x-i
        v += i
    y-i
        v += i
    i++
'''