with open('d2p1.in') as f:
    directions = f.read().split('\n')

code = []
number = 5

def up(num: int) -> int:
    if num in [5, 2, 1, 4, 9]:
        return num
    elif num == 3:
        return 1
    else:
        return num - 4

def down(num: int) -> int:
    if num in [5, 10, 15, 12, 9]:
        return num
    else:
        return num + 4

def left(num: int) -> int:
    if num in [1, 2, 5, 10, 15]:
        return num
    else:
        return num - 1

def right(num: int) -> int:
    if num in [1, 4, 9, 12, 15]:
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