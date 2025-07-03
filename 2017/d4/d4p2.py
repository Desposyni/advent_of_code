from re import search

def red(text):
    return f'\033[91m{text}\033[0m'

def green(text):
    return f'\033[92m{text}\033[0m'

with open('d4p1.in') as f:
    passwords = f.read().split('\n')

passphrases = []

for password in passwords:
    print(password)
    words = password.split()
    print(words)
    words = [''.join(sorted(word)) for word in words]
    print(words)
    for word in words:
        if words.count(word) > 1:
            print(red(password))
            break
    else:
        passphrases.append(password)
        print(green(password))

print(len(passphrases))