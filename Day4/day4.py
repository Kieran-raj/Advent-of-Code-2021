def check_rows(board):
    for row in board:
        num_strings = 0
        num_ints = 0
        for element in row:
            if isinstance(element, int):
                num_ints += 1
            else:
                num_strings += 1
        if num_strings > 0:
            continue
        else:
            return True

    return False


def check_columns(board):
    columns = []
    for i in range(5):
        column = [row[i] for row in board]
        columns.append(column)

    for col in columns:
        num_strings = 0
        num_ints = 0
        for element in col:
            if isinstance(element, int):
                num_ints += 1
            else:
                num_strings += 1
        if num_strings > 0:
            continue
        else:
            return True
    return False


global_boards = []


def check_for_nums_part1(number, boards):
    global global_boards
    checked_boards = []
    for board in boards:
        checked_board = []
        for row in board:
            checked_row = [element if int(element) != number else int(element)
                           for element in row]
            checked_board.append(checked_row)
        checked_boards.append(checked_board)
    for board in checked_boards:
        if not check_rows(board):
            if not check_columns(board):
                global_boards = checked_boards
            else:
                return (True, board)
            global_boards = checked_boards
        else:
            return (True, board)


def calculation(board, num):
    unmarked_values = []
    for row in board:
        for element in row:
            if isinstance(element, str):
                unmarked_values.append(int(element))

    return sum(unmarked_values) * num


with open('rand_nums.txt', 'r') as file:
    rand_nums = file.readline().strip().split(',')

with open('boards.txt', 'r') as file:
    raw_boards = [line.strip().split(' ') for line in file.readlines()]
    filtered_boards = []
    for row in raw_boards:
        new_row = []
        for element in row:
            if element != '':
                new_row.append(element)
        if len(new_row) > 0:
            filtered_boards.append(new_row)

    global_boards = []
    for j in range(0, len(filtered_boards), 5):
        global_boards.append(filtered_boards[j:j+5])


# part 1
for i in rand_nums:
    check = check_for_nums_part1(int(i), global_boards)
    if check:
        if check[0]:
            print(calculation(check[1], int(i)))
            break
