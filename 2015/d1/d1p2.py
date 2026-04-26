with open("d1p1.in") as f:
    instructions = f.read()

current_floor = 0
for x, i in enumerate(instructions, start=1):
    # if i == "(":
    #     current_floor += 1
    # elif i == ")":
    #     current_floor -= 1
    current_floor += 1 if i == "(" else -1
    if current_floor < 0:
        break

print("current floor is", current_floor, "position is", x)
