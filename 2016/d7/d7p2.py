from re import findall

with open('d7p1.in') as f:
    addresses = f.read().split('\n')

ssl_addresses = []

for address in addresses:
    abas = findall(r'(?=(\w)(?!\1)(\w)\1(?!\w*?]))', address)
    for a, b in abas:
        bab = findall(rf'{b+a+b}(?=\w*?])', address)
        if bab:
            ssl_addresses.append(address)
            break
print(len(ssl_addresses))