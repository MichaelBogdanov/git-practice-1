"""Тесты для задачи 11 — Проверка шахматного хода."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from solution import parse_board, check_move


def make_board(rows: list[str]) -> list[list[str]]:
    return parse_board(rows)


def empty_board() -> list[list[str]]:
    return make_board(["........"] * 8)


def place(board, piece, row, col):
    board[row][col] = piece
    return board


# ---- Ладья ----

def test_rook_valid_horizontal():
    b = empty_board()
    place(b, "R", 4, 0)
    assert check_move(b, (4, 0), (4, 5))


def test_rook_blocked():
    b = empty_board()
    place(b, "R", 4, 0)
    place(b, "P", 4, 3)  # белая пешка блокирует
    assert not check_move(b, (4, 0), (4, 5))


def test_rook_capture():
    b = empty_board()
    place(b, "R", 4, 0)
    place(b, "p", 4, 3)  # чёрная пешка — можно взять
    assert check_move(b, (4, 0), (4, 3))


# ---- Конь ----

def test_knight_valid():
    b = empty_board()
    place(b, "N", 4, 4)
    assert check_move(b, (4, 4), (2, 5))


def test_knight_jump_over():
    b = empty_board()
    place(b, "N", 4, 4)
    # Заполняем соседние клетки — конь всё равно прыгает
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            place(b, "P", 4 + dr, 4 + dc)
    place(b, "N", 4, 4)  # восстанавливаем коня
    assert check_move(b, (4, 4), (2, 5))


# ---- Пешка ----

def test_pawn_white_one_step():
    b = empty_board()
    place(b, "P", 4, 4)
    assert check_move(b, (4, 4), (3, 4))


def test_pawn_white_two_steps_from_start():
    b = empty_board()
    place(b, "P", 6, 4)
    assert check_move(b, (6, 4), (4, 4))


def test_pawn_blocked():
    b = empty_board()
    place(b, "P", 4, 4)
    place(b, "p", 3, 4)  # заблокирована чёрной
    assert not check_move(b, (4, 4), (3, 4))


def test_pawn_capture_diagonal():
    b = empty_board()
    place(b, "P", 4, 4)
    place(b, "p", 3, 5)
    assert check_move(b, (4, 4), (3, 5))


# ---- Король ----

def test_king_one_step():
    b = empty_board()
    place(b, "K", 4, 4)
    assert check_move(b, (4, 4), (4, 5))
    assert check_move(b, (4, 4), (3, 3))


def test_king_two_steps_invalid():
    b = empty_board()
    place(b, "K", 4, 4)
    assert not check_move(b, (4, 4), (4, 6))


# ---- Ферзь ----

def test_queen_diagonal():
    b = empty_board()
    place(b, "Q", 0, 0)
    assert check_move(b, (0, 0), (7, 7))


# ---- Общее ----

def test_empty_square():
    b = empty_board()
    assert not check_move(b, (4, 4), (4, 5))


def test_same_square():
    b = empty_board()
    place(b, "R", 4, 4)
    assert not check_move(b, (4, 4), (4, 4))


if __name__ == "__main__":
    tests = [
        test_rook_valid_horizontal, test_rook_blocked, test_rook_capture,
        test_knight_valid, test_knight_jump_over,
        test_pawn_white_one_step, test_pawn_white_two_steps_from_start,
        test_pawn_blocked, test_pawn_capture_diagonal,
        test_king_one_step, test_king_two_steps_invalid,
        test_queen_diagonal,
        test_empty_square, test_same_square,
    ]
    passed = 0
    for t in tests:
        try:
            t()
            print(f"PASS: {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {t.__name__} — {e}")
    print(f"\n{passed}/{len(tests)} тестов прошло")
