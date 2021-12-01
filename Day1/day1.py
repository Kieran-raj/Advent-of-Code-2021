# Part 1
with open('input.txt', 'r') as file:
    lines = [int(i.strip()) for i in file.readlines()]
    count = 0
    for idx, _ in enumerate(lines):
        if lines[idx] > lines[idx - 1]:
            count += 1
    print(count)

# Part 2
with open('input.txt', 'r') as file:
    lines = [int(i.strip()) for i in file.readlines()]
    count = 0
    for idx, _ in enumerate(lines):
        if sum(lines[idx + 1: idx + 4]) > sum(lines[idx: idx + 3]):
            count += 1
    print(count)
