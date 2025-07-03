with open('d6p1.in') as f:
    banks = [int(i) for i in f.read().split()]
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