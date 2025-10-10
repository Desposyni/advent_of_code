from re import findall

with open('d7p1.in') as f:
    addresses = f.read().split('\n')

tls_addresses = []

for address in addresses:
    palindrome = findall(r'(\w)(?!\1)(\w)\2\1(?!\w*?])', address)
    bad = findall(r'(\w)(?!\1)(\w)\2\1(?=\w*?])', address)
    if palindrome and not bad:
        tls_addresses.append(address)
print(len(tls_addresses))