from re import findall

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
    for requirement in required:
        if requirement not in passport:
            break
    else:
        try:
            height, unit = findall(r'(\d+)(cm|in)', passport['hgt'])[0]
        except:
            height, unit = 1, 'cm'
        hair = findall(r'^#[0-9a-f]{6}$', passport['hcl'])
        pid = findall(r'^\d{9}$', passport['pid'])
        conditions = (1920 <= int(passport['byr']) <= 2002,
                      2010 <= int(passport['iyr']) <= 2020,
                      2020 <= int(passport['eyr']) <= 2030,
                      150 <= int(height) <= 193 if unit == 'cm' else 59 <= int(height) <= 76 if unit == 'in' else False,
                      hair,
                      passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
                      pid,
                      )
        if all(conditions):
            valid_passports += 1

print(f'{valid_passports = }')