OPPOSITE = {
    "NORTH": "SOUTH",
    "SOUTH": "NORTH",
    "EAST": "WEST",
    "WEST": "EAST"
}


def dirReduc(arr):
    stack = []
    for direction in arr:
        if stack and stack[-1] == OPPOSITE[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack
