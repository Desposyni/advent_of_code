with open('d2p1.in') as f:
    opcodes = [int(opcode) for opcode in f.read().split(',')]

opcodes[1] = 12
opcodes[2] = 2

for i in range(0, len(opcodes)-1, 4):
    op = opcodes[i]
    if op == 99: break
    a = opcodes[opcodes[i+1]]
    b = opcodes[opcodes[i+2]]
    c = opcodes[i+3]

    opcodes[c] = a+b if op == 1 else a*b

print(opcodes[0])