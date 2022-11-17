import os


def extract_data():
    file = open(os.path.dirname(
        os.path.realpath(__file__)) + "/input.txt", "r")
    bingo_numbers = []
    boards = []
    board = []
    b = 0
    for line in file:
        line = line.strip()
        if len(line) > 0:
            if len(bingo_numbers) == 0:
                for num in line.split(','):
                    bingo_numbers.append(int(num))
                continue

            board.append([])
            for num in line.split():
                board[b].append(int(num))
            b = b+1
        elif len(board) > 0:
            boards.append(board)
            board = []
            b = 0

    return (bingo_numbers, boards)


def check(board):
    for line in board:
        bingo = True
        for n in line:
            if n is not None:
                bingo = False
                continue
        if bingo:
            return True

    for l in range(5):
        for c in range(5):
            bingo = True
            if board[l][c] is not None:
                bingo = False
                continue
        if bingo:
            return True

    return False


def count_numbers(board):
    count = 0
    for line in board:
        for num in line:
            if num is not None:
                count = count + num

    return count


def part1():
    (bingo_numbers, boards) = extract_data()
    for num in bingo_numbers:
        for board in boards:
            for line in board:
                for idx, n in enumerate(line):
                    if n == num:
                        line[idx] = None
                        continue
            if check(board):
                return num * count_numbers(board)


print("part1: {0}".format(part1()))
