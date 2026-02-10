def read_board(filename):
    board = []
    with open(filename, "r") as f:
        for line in f:
            board.append(list(line.strip()))
    return board


def is_valid_rook_move(board, x1, y1, x2, y2):
    if x1 != x2 and y1 != y2:
        return False

    dx = 0
    dy = 0

    if x1 < x2:
        dx = 1
    elif x1 > x2:
        dx = -1

    if y1 < y2:
        dy = 1
    elif y1 > y2:
        dy = -1

    x = x1 + dx
    y = y1 + dy

    while x != x2 or y != y2:
        if board[x][y] != ".":
            return False
        x += dx
        y += dy

    return True


def main():
    board = read_board("board.txt")

    x1, y1 = 4, 4   # откуда
    x2, y2 = 1, 4   # куда

    piece = board[x1][y1]

    if piece == ".":
        print("INVALID")
        return

    if piece.upper() == "R":
        if is_valid_rook_move(board, x1, y1, x2, y2):
            print("VALID")
        else:
            print("INVALID")
    else:
        print("INVALID")


main()
