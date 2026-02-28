import sys

col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

def read_board(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) != 8:
        raise ValueError("Доска должна содержать ровно 8 строк")
    board = [list(line) for line in lines]
    return board

def parse_position(pos):
    if len(pos) != 2 or pos[0] not in col_map or not pos[1].isdigit():
        raise ValueError("Неверный формат позиции. Ожидается буква+цифра, например e2")
    col = col_map[pos[0]]
    row = 8 - int(pos[1])   
    return row, col

def is_inside(r, c):
    return 0 <= r < 8 and 0 <= c < 8

def is_path_clear(board, fr, fc, tr, tc):

    dr = (tr - fr)
    dc = (tc - fc)
    step_r = 0 if dr == 0 else (1 if dr > 0 else -1)
    step_c = 0 if dc == 0 else (1 if dc > 0 else -1)
    r, c = fr + step_r, fc + step_c
    while (r, c) != (tr, tc):
        if board[r][c] != '.':
            return False
        r += step_r
        c += step_c
    return True

def is_valid_move(board, fr, fc, tr, tc):
    if not (is_inside(fr, fc) and is_inside(tr, tc)):
        return False

    piece = board[fr][fc]
    target = board[tr][tc]
    if piece == '.':
        return False
    piece_is_white = piece.isupper()
    target_is_white = target.isupper() if target != '.' else None
    if target != '.' and piece_is_white == target_is_white:
        return False
    p = piece.upper()

    dr = tr - fr
    dc = tc - fc

    if p == 'K':
        if max(abs(dr), abs(dc)) == 1:
            return True

    elif p == 'Q':
        if (dr == 0 or dc == 0 or abs(dr) == abs(dc)) and is_path_clear(board, fr, fc, tr, tc):
            return True

    elif p == 'R':
        if (dr == 0 or dc == 0) and is_path_clear(board, fr, fc, tr, tc):
            return True

    elif p == 'B':
        if abs(dr) == abs(dc) and is_path_clear(board, fr, fc, tr, tc):
            return True

    elif p == 'N':
        if (abs(dr), abs(dc)) in [(1, 2), (2, 1)]:
            return True

    elif p == 'P':
        direction = -1 if piece_is_white else 1   
        start_row = 6 if piece_is_white else 1   

        if dc == 0:
            if dr == direction and target == '.':
                return True
            if fr == start_row and dr == 2 * direction and target == '.' and board[fr + direction][fc] == '.':
                return True
        if abs(dc) == 1 and dr == direction and target != '.' and piece_is_white != target_is_white:
            return True
    return False

def main():
    if len(sys.argv) != 4:
        print("Использование: python solution.py <файл_доски> <начало> <конец>")
        print("Пример: python solution.py board.txt e2 e4")
        sys.exit(1)

    board_file = sys.argv[1]
    start = sys.argv[2].lower()
    end = sys.argv[3].lower()

    try:
        board = read_board(board_file)
        fr, fc = parse_position(start)
        tr, tc = parse_position(end)
    except Exception as e:
        print("Ошибка ввода:", e)
        print("INVALID")
        return

    if is_valid_move(board, fr, fc, tr, tc):
        print("VALID")
    else:
        print("INVALID")

if __name__ == "__main__":
    main()