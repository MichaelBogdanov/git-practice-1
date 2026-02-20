def load_board(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def is_valid_move(board, r1, c1, r2, c2):
    piece = board[r1][c1]

    if piece == '.':
        return False

    target = board[r2][c2]

    if target != '.' and piece.isupper() == target.isupper():
        return False

    dr = r2 - r1
    dc = c2 - c1

    piece_type = piece.upper()

    # Пешка
    if piece_type == 'P':
        direction = -1 if piece.isupper() else 1
        start_row = 6 if piece.isupper() else 1

        # обычный ход
        if dc == 0 and dr == direction and target == '.':
            return True
        # двойной ход
        if dc == 0 and r1 == start_row and dr == 2 * direction and board[r1 + direction][c1] == '.' and target == '.':
            return True
        # взятие
        if abs(dc) == 1 and dr == direction and target != '.':
            return True
        return False

    # Конь
    if piece_type == 'N':
        return (abs(dr), abs(dc)) in [(1, 2), (2, 1)]

    # Король
    if piece_type == 'K':
        return max(abs(dr), abs(dc)) == 1

    # Ладья
    if piece_type == 'R':
        if dr != 0 and dc != 0:
            return False
        step_r = (dr > 0) - (dr < 0)
        step_c = (dc > 0) - (dc < 0)
        r, c = r1 + step_r, c1 + step_c
        while (r, c) != (r2, c2):
            if board[r][c] != '.':
                return False
            r += step_r
            c += step_c
        return True

    # Слон
    if piece_type == 'B':
        if abs(dr) != abs(dc):
            return False
        step_r = (dr > 0) - (dr < 0)
        step_c = (dc > 0) - (dc < 0)
        r, c = r1 + step_r, c1 + step_c
        while (r, c) != (r2, c2):
            if board[r][c] != '.':
                return False
            r += step_r
            c += step_c
        return True

    # Ферзь
    if piece_type == 'Q':
        if dr == 0 or dc == 0:
            return is_valid_move(board, r1, c1, r2, c2)  # как ладья
        if abs(dr) == abs(dc):
            return is_valid_move(board, r1, c1, r2, c2)  # как слон
        return False

    return False


board = load_board("board.txt")

r1, c1 = 6, 4  # откуда
r2, c2 = 4, 4  # куда

print("VALID" if is_valid_move(board, r1, c1, r2, c2) else "INVALID")