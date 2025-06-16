with open('d2p1.in') as f:
    rows = f.read().split('\n')

rows = [sorted(list(map(int, row.split())), reverse=True) for row in rows]

checksum = 0
for row in rows:
    found = False
    for i, big_num in enumerate(row):
        for small_num in row[:i:-1]:
            if big_num % small_num == 0:
                checksum += big_num // small_num
                found = True
                break
        if found: break

print(checksum)