from re import findall

class Program:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.carrying = []

    def __repr__(self):
        return f'{self.name} ({self.weight}) {self.carrying}'

with open('d7p1.in') as f:
    info = f.read()

programs = [Program(p, int(i)) for p, i in findall(r'(\w+) \((\d+)\)', info)]
print(programs)