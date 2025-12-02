from re import findall

with open('d2p1.in') as f:
    products = [(int(x), int(y)) for x, y in findall(r'(\d+)-(\d+)', f.read())]
print(products)

invalid = []
for start, stop in products:
    for product in range(start, stop + 1):
        num = str(product)
        if findall(r'^(\d+)(\1)$', num):
            invalid.append(product)
print(invalid)
print(sum(invalid))