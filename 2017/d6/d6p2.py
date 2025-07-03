with open('d6p1.in') as f:
    banks = [int(i) for i in f.read().split()]
banks = [0, 14, 13, 12, 11, 10, 8, 8, 6, 6, 5, 3, 3, 2, 1, 10]
seen = [banks[:]]
print(seen)
while True:
    max_size = max(banks)
    print(max_size)
    max_index = banks.index(max_size)
    print(max_index)
    banks[max_index] = 0
    print(banks)
    while max_size > 0:
        max_index += 1
        banks[max_index % 16] += 1
        print(banks)
        max_size -= 1
    if banks in seen:
        print(len(seen))
        break
    else:
        seen.append(banks[:])
        print(seen)