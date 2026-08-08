with open("d1p1.in") as f:
    instructions = f.read()

current_floor = 0
for i in instructions:
    # if i == "(":
    #     current_floor += 1
    # elif i == ")":
    #     current_floor -= 1
    current_floor += 1 if i == "(" else -1

print("current floor is", current_floor)
