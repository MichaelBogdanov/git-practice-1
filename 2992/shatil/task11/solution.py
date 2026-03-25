"""
Задача 11 — Проверка шахматного хода

Считывает из файла:
  - 8 строк по 8 символов — состояние доски
  - строку с ходом вида: "e2 e4"  (столбец буква a-h, строка цифра 1-8)

Обозначения фигур:
  Заглавные — белые, строчные — чёрные
  K/k — Король, Q/q — Ферзь, R/r — Ладья,
  B/b — Слон, N/n — Конь, P/p — Пешка, . — пустая клетка

Вывод: VALID или INVALID
"""

import sys

# Направления для каждой фигуры (кроме пешки и коня)
ROOK_DIRS   = [(1, 0), (-1, 0), (0, 1), (0, -1)]
BISHOP_DIRS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
QUEEN_DIRS  = ROOK_DIRS + BISHOP_DIRS
KING_MOVES  = QUEEN_DIRS  # ровно 1 шаг
KNIGHT_MOVES = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2),
]


def parse_board(lines: list[str]) -> list[list[str]]:
    """Парсит 8 строк в двумерный список board[row][col]."""
    board = []
    for line in lines[:8]:
        row = list(line.rstrip("\n"))
        # Дополняем до 8, если строка короче
        while len(row) < 8:
            row.append(".")
        board.append(row[:8])
    return board


def parse_move(move_str: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Парсит ход вида 'e2 e4'.
    Возвращает ((row_from, col_from), (row_to, col_to)).
    row 0 = верхняя строка доски (8-я шахматная rank), col 0 = столбец a.
    """
    parts = move_str.strip().split()
    if len(parts) != 2:
        raise ValueError(f"Неверный формат хода: '{move_str}'")

    def algebraic_to_rc(pos: str) -> tuple[int, int]:
        if len(pos) != 2:
            raise ValueError(f"Неверная позиция: '{pos}'")
        col = ord(pos[0].lower()) - ord("a")
        rank = int(pos[1])          # 1–8
        row = 8 - rank              # rank 8 → row 0, rank 1 → row 7
        return row, col

    return algebraic_to_rc(parts[0]), algebraic_to_rc(parts[1])


def is_white(piece: str) -> bool:
    return piece.isupper()


def is_empty(piece: str) -> bool:
    return piece == "."


def same_color(p1: str, p2: str) -> bool:
    """True если обе фигуры одного цвета."""
    return not is_empty(p1) and not is_empty(p2) and is_white(p1) == is_white(p2)


def in_bounds(r: int, c: int) -> bool:
    return 0 <= r < 8 and 0 <= c < 8


def sliding_moves(board, fr, fc, directions) -> set[tuple[int, int]]:
    """
    Генерирует все клетки, достижимые скользящей фигурой
    по заданным направлениям (до первого препятствия).
    """
    piece = board[fr][fc]
    reachable = set()
    for dr, dc in directions:
        r, c = fr + dr, fc + dc
        while in_bounds(r, c):
            target = board[r][c]
            if is_empty(target):
                reachable.add((r, c))
            else:
                if not same_color(piece, target):
                    reachable.add((r, c))  # взятие
                break
            r += dr
            c += dc
    return reachable


def valid_moves(board: list[list[str]], fr: int, fc: int) -> set[tuple[int, int]]:
    """Возвращает множество допустимых клеток назначения для фигуры на (fr, fc)."""
    piece = board[fr][fc]
    p = piece.lower()
    white = is_white(piece)

    if p == "r":
        return sliding_moves(board, fr, fc, ROOK_DIRS)

    if p == "b":
        return sliding_moves(board, fr, fc, BISHOP_DIRS)

    if p == "q":
        return sliding_moves(board, fr, fc, QUEEN_DIRS)

    if p == "k":
        moves = set()
        for dr, dc in KING_MOVES:
            r, c = fr + dr, fc + dc
            if in_bounds(r, c) and not same_color(piece, board[r][c]):
                moves.add((r, c))
        return moves

    if p == "n":
        moves = set()
        for dr, dc in KNIGHT_MOVES:
            r, c = fr + dr, fc + dc
            if in_bounds(r, c) and not same_color(piece, board[r][c]):
                moves.add((r, c))
        return moves

    if p == "p":
        moves = set()
        # Белые движутся вверх (row убывает), чёрные — вниз (row возрастает)
        direction = -1 if white else 1
        start_row = 6 if white else 1  # начальная позиция для двойного хода

        # Ход вперёд на 1
        r1 = fr + direction
        if in_bounds(r1, fc) and is_empty(board[r1][fc]):
            moves.add((r1, fc))
            # Ход вперёд на 2 из начальной позиции
            r2 = fr + 2 * direction
            if fr == start_row and in_bounds(r2, fc) and is_empty(board[r2][fc]):
                moves.add((r2, fc))

        # Взятие по диагонали
        for dc in (-1, 1):
            r, c = fr + direction, fc + dc
            if in_bounds(r, c) and not is_empty(board[r][c]) and not same_color(piece, board[r][c]):
                moves.add((r, c))

        return moves

    return set()


def check_move(board: list[list[str]], from_pos: tuple, to_pos: tuple) -> bool:
    """Возвращает True если ход допустим."""
    fr, fc = from_pos
    tr, tc = to_pos

    # Позиции должны быть в пределах доски
    if not (in_bounds(fr, fc) and in_bounds(tr, tc)):
        return False

    piece = board[fr][fc]

    # На начальной клетке должна стоять фигура
    if is_empty(piece):
        return False

    # Ход не на ту же клетку
    if from_pos == to_pos:
        return False

    return to_pos in valid_moves(board, fr, fc)


def main():
    if len(sys.argv) < 2:
        print("Использование: python solution.py <файл>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) < 9:
        print("INVALID")
        return

    board = parse_board(lines[:8])

    try:
        from_pos, to_pos = parse_move(lines[8])
    except (ValueError, IndexError):
        print("INVALID")
        return

    result = check_move(board, from_pos, to_pos)
    print("VALID" if result else "INVALID")


if __name__ == "__main__":
    main()
