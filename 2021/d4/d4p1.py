from itertools import batched

with open('d4p1.in') as f:
    draws = f.readline().strip().split(',')
    lines = [line.strip() for line in f.readlines() if line != '\n']
    
boards = []
for line in lines:
    nums = line.split()
    for num in nums:
        boards.append({'num': int(num), 'state': False})

boards = list(batched(list(batched(boards, 5)), 5))
# boards[0][0][0]['state'] = True 

print(boards)
