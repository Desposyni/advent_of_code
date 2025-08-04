with open("d1p1.in") as file:
    numbers = file.read().split('\n')

freq = 0
past_freq = []

for number in numbers:
    freq += int(number)

print(freq)