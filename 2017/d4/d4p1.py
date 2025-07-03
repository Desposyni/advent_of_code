from re import search

def red(text):
    return f'\033[91m{text}\033[0m'

def green(text):
    return f'\033[92m{text}\033[0m'

with open('d4p1.in') as f:
    passwords = f.read().split('\n')

passphrases = []

for password in passwords:
    bad_phrase = search(r'\b(\w+)\b.+?\b(\1)\b', password)
    if not bad_phrase:
        print(green(password))
        passphrases.append(password)
    else:
        print(red(password))

print(len(passphrases))