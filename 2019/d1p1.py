with open('d1p1.in') as f:
    modules = [int(module) for module in f.read().split('\n')]

fuels = [module // 3 - 2 for module in modules]
total_fuel = sum(fuels)

print(f'{total_fuel = }')