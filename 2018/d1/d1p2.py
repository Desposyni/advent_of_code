from itertools import cycle

with open("d1p1.in") as file:
    numbers = file.read().split('\n')

freq = 0
past_freq = [0]

for number in cycle(numbers):
    freq += int(number)
    print(freq)
    if freq in past_freq: break
    past_freq.append(freq)

print(freq, 'is a duplicate')