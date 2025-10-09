from hashlib import md5
from itertools import count

door_id = 'uqwqemis'
password = ['x' for _ in range(8)]
c = count()
positions = []

while 'x' in password:
    i = c.__next__()
    md5sum = md5(f'{door_id}{i}'.encode()).hexdigest()
    if md5sum[:5] == '0' * 5:
        position = int(md5sum[5], 16)
        if 0 <= position < 8:
            if position not in positions:
                positions.append(position)
                password[position] = md5sum[6]
                print(f'{"".join(password)}, {i = }, {md5sum = }')

print('password =', ''.join(password))