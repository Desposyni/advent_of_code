with open('d2p1.in') as f:
    directions = f.read().split('\n')

code = []
number = 5

def up(num: int) -> int:
    if num in [1, 2, 3]:
        return num
    else:
        return num - 3

def down(num: int) -> int:
    if num in [7, 8, 9]:
        return num
    else:
        return num + 3

def left(num: int) -> int:
    if num in [1, 4, 7]:
        return num
    else:
        return num - 1

def right(num: int) -> int:
    if num in [3, 6, 9]:
        return num
    else:
        return num + 1

for line in directions:
    for letter in line:
        match letter:
            case 'U':
                number = up(number)
            case 'D':
                number = down(number)
            case 'L':
                number = left(number)
            case 'R':
                number = right(number)
    code.append(number)
print(code)