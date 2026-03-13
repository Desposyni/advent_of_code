from collections import Counter

with open('d3p1.in') as f:
    reports = f.read().split("\n")

columns = zip(*reports)
gamma = []
for column in columns:
    gamma.append(Counter(column).most_common(1)[0][0])
gamma = ''.join(gamma)
gamma = int(gamma, base=2)
epsilon = 4095 ^ gamma
print(gamma * epsilon)