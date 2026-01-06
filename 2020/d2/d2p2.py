from os.path import split

with open('d2p1.in') as f:
    passwords = f.read().split('\n')

print(passwords)
counter = 0
for password in passwords:
    num, letter, passwd = password.split(' ')
    first_num, second_num = num.split('-')
    first_num = int(first_num)
    second_num = int(second_num)
    letter = letter[0]
    first_pass = passwd[first_num - 1]
    second_pass = passwd[second_num - 1]
    print(first_num, second_num, letter, first_pass, second_pass, passwd)
    if (letter == first_pass) ^ (letter == second_pass):
        print('yes!')
        counter += 1
    else:
        print('sorry, too many/not enough', letter)
print(counter)