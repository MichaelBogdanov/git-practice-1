import os
import sys

# a-h -> 0-7
col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
           'e': 4, 'f': 5, 'g': 6, 'h': 7}


def read_board(filename='input.txt'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, filename)

    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    if len(lines) != 8:
        raise ValueError("Доска должна содержать ровно 8 строк")

    board = [list(line) for line in lines]
    return board


def parse_position(pos: str):
    pos = pos.strip().lower()
    if len(pos) != 2 or pos[0] not in col_map or not pos[1].isdigit():
        raise ValueError("Неверный формат позиции. Ожидается буква+цифра, например e2")
    col = col_map[pos[0]]
    row_num = int(pos[1])
    if not (1 <= row_num <= 8):
        raise ValueError("Номер строки должен быть от 1 до 8")
    # В файле 0-я строка -8-я горизонталь, значит row = 8 - номер
    row = 8 - row_num
    return row, col


def is_inside(r, c):
    return 0 <= r < 8 and 0 <= c < 8


def is_path_clear(board, fr, fc, tr, tc):
    """Путь для ладьи/слона/ферзя: между from и to не должно быть фигур."""
    dr = tr - fr
    dc = tc - fc

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
        # с пустой клетки ходить нельзя
        return False

    piece_is_white = piece.isupper()
    target_is_white = target.isupper() if target != '.' else None

    # нельзя бить свою фигуру
    if target != '.' and piece_is_white == target_is_white:
        return False

    p = piece.upper()
    dr = tr - fr
    dc = tc - fc

    # Король
    if p == 'K':
        if max(abs(dr), abs(dc)) == 1:
            return True

    # Ферзь
    elif p == 'Q':
        if (dr == 0 or dc == 0 or abs(dr) == abs(dc)) and is_path_clear(board, fr, fc, tr, tc):
            return True

    # Ладья
    elif p == 'R':
        if (dr == 0 or dc == 0) and is_path_clear(board, fr, fc, tr, tc):
            return True

    # Слон
    elif p == 'B':
        if abs(dr) == abs(dc) and is_path_clear(board, fr, fc, tr, tc):
            return True

    # Конь
    elif p == 'N':
        if (abs(dr), abs(dc)) in [(1, 2), (2, 1)]:
            return True

    # Пешка
    elif p == 'P':
        direction = -1 if piece_is_white else 1  # белые вверх (к меньшим r), чёрные вниз
        start_row = 6 if piece_is_white else 1   # 2-я и 7-я горизонтали

        # Ход вперёд
        if dc == 0:
            # на одну клетку
            if dr == direction and target == '.':
                return True
            # на две клетки со стартовой позиции, путь должен быть пуст
            if fr == start_row and dr == 2 * direction and target == '.' and board[fr + direction][fc] == '.':
                return True

        # Взятие по диагонали
        if abs(dc) == 1 and dr == direction and target != '.' and piece_is_white != target_is_white:
            return True

    return False


def main():
    if len(sys.argv) != 3:
        print("Использование: python solution.py <начало> <конец>")
        sys.exit(1)

    start = sys.argv[1]
    end = sys.argv[2]

    try:
        board = read_board('input.txt')
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
