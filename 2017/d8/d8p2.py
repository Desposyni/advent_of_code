from collections import defaultdict
from re import match

with open('d8p1.in') as f:
    instructs = f.read().split('\n')

registers = defaultdict(int)
instruct_regex = r'(\w+) (inc|dec) (-?\d+) if (\w+) (\W+) (-?\d+)'
max_val = 0

for instruct in instructs:
    reg, mod, amt, reg_chk, mod_chk, amt_chk = match(instruct_regex, instruct).groups()
    amt, amt_chk = int(amt), int(amt_chk)

    if eval(f'registers["{reg_chk}"] {mod_chk} {amt_chk}'):
        registers[reg] += amt if mod == 'inc' else amt * -1
        if (temp_max := max(registers.values())) > max_val: max_val = temp_max

print(max_val)