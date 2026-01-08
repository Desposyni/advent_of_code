with open('d4p1.in') as f:
    scans = [sorted(i.split()) for i in f.read().split('\n\n')]

valid_passports = 0
passports = []
for scan in scans:
    passports.append({})
    for i in scan:
        k, v = i.split(':')
        passports[-1][k] = v
required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
for passport in passports:
    print(passport)
    for requirement in required:
        if requirement not in passport:
            print(requirement, 'missing')
            break
    else:
        valid_passports += 1

print(f'{valid_passports = }')