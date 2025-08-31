with open('d1p1.in') as f:
    modules: list[int] = [int(module) for module in f.read().split('\n')]

def calc_fuel(mass: int) -> int:
    return mass // 3 - 2 if mass > 8 else 0

fuels: list[int] = [calc_fuel(module) for module in modules]
module_fuels = sum(fuels)

fuel_fuel = 0
for fuel in fuels:
    while extra := calc_fuel(fuel):
        fuel_fuel += extra
        fuel = extra

all_fuel = module_fuels + fuel_fuel
print(f'{all_fuel = }')