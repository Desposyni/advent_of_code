from hashlib import md5
from itertools import count

door_id = 'uqwqemis'
password = []
c = count()

while len(password) < 8:
    i = c.__next__()
    md5sum = md5(f'{door_id}{i}'.encode()).hexdigest()
    if md5sum[:5] == '0' * 5:
        password.append(md5sum[5])
        print(f'{password[-1]}, {i = }, {md5sum = }')

print('password =', ''.join(password))