with open('d2p1.in') as f:
    rows = f.read().split('\n')

rows = [list(map(int, row.split())) for row in rows]

checksum = 0

for row in rows:
    checksum += max(row) - min(row)

print(checksum)