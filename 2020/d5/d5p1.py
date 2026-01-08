with open('d5p1.in') as f:
    seats = f.read().split('\n')

seat_ids = []
for seat in seats:
    print(seat)
    print(seat[:7][::-1], seat[7:][::-1])
    row = 0
    for i, r in enumerate(seat[:7][::-1]):
        print(i, r)
        if r == 'B': row += 2 ** i

    col = 0
    for i, c in enumerate(seat[7:][::-1]):
        print(i, c)
        if c == 'R': col += 2 ** i

    print(row, col, row * 8 + col)
    seat_ids.append(row * 8 + col)

print(f'{max(seat_ids) = }')