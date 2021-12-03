# part 1
with open('input.txt', 'r') as file:
    depth = 0
    horizontal = 0
    lines = [line.strip().split() for line in file.readlines()]

    for move in lines:
        if move[0] == 'forward':
            horizontal += int(move[1])
        elif move[0] == 'up':
            depth -= int(move[1])
        else:
            depth += int(move[1])

total = depth * horizontal

print(total)

# part 2
with open('input.txt', 'r') as file:
    depth = 0
    horizontal = 0
    aim = 0
    lines = [line.strip().split() for line in file.readlines()]

    for move in lines:
        if move[0] == 'forward':
            horizontal += int(move[1])
            depth += aim * int(move[1])
        elif move[0] == 'up':
            aim -= int(move[1])
        else:
            aim += int(move[1])

total = depth * horizontal

print(total)
