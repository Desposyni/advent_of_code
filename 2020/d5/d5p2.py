with open('d5p1.in') as f:
    seats = f.read().split('\n')

seat_ids = []
for seat in seats:
    row = 0
    for i, r in enumerate(seat[:7][::-1]):
        if r == 'B': row += 2 ** i

    col = 0
    for i, c in enumerate(seat[7:][::-1]):
        if c == 'R': col += 2 ** i

    seat_ids.append(row * 8 + col)

print(f'{max(seat_ids) = }')
# look for a number between 9 and 850 that is not in seat_ids
for i in range(858):
    if i not in seat_ids and i+1 in seat_ids and i-1 in seat_ids:
        print(i)