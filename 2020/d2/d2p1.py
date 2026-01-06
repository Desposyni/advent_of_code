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
    num_of_letters = passwd.count(letter)
    print(first_num, second_num, letter, passwd, num_of_letters)
    if first_num <= num_of_letters <= second_num:
        print('yes!')
        counter += 1
    else:
        print('sorry, too many/not enough', letter)
print(counter)