def main():
    # Чтение доски из файла input.txt
    try:
        with open('input.txt', 'r') as f:
            board = [list(line.rstrip('\n')) for line in f.readlines()]
    except FileNotFoundError:
        print("No")
        return

    # Проверка размера доски
    if len(board) != 8 or any(len(row) != 8 for row in board):
        print("No")
        return

    # Направления для разных фигур
    directions = {
        'rook': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'bishop': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'queen': [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)],
        'king': [(-1, 0), (1, 0), (0, -1), (0, 1),
                 (-1, -1), (-1, 1), (1, -1), (1, 1)],
        'knight': [(2, 1), (2, -1), (-2, 1), (-2, -1),
                   (1, 2), (1, -2), (-1, 2), (-1, -2)]
    }

    def inside(r, c):
        """Проверка, находятся ли координаты в пределах доски."""
        return 0 <= r < 8 and 0 <= c < 8

    def get_color(piece):
        """Возвращает цвет фигуры: True для белых, False для чёрных, None для пустой клетки."""
        if piece == '.':
            return None
        return piece.isupper()   # заглавные – белые

    # Перебираем все клетки доски
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == '.':
                continue
            color = get_color(piece)   # True – белые, False – чёрные
            p_low = piece.lower()

            # Пешка
            if p_low == 'p':
                dr = -1 if color else 1   # белые вверх (уменьшение r)
                # ход на одну клетку вперёд
                nr, nc = r + dr, c
                if inside(nr, nc) and board[nr][nc] == '.':
                    print("Yes")
                    return
                # ход на две клетки с начальной позиции
                if (color and r == 6) or (not color and r == 1):
                    nr2 = r + 2 * dr
                    if inside(nr2, nc) and board[nr][nc] == '.' and board[nr2][nc] == '.':
                        print("Yes")
                        return
                # взятие вправо и влево
                for dc in (-1, 1):
                    nr, nc = r + dr, c + dc
                    if inside(nr, nc):
                        target = board[nr][nc]
                        if target != '.' and get_color(target) != color:
                            print("Yes")
                            return

            # Конь
            elif p_low == 'n':
                for dr, dc in directions['knight']:
                    nr, nc = r + dr, c + dc
                    if inside(nr, nc):
                        target = board[nr][nc]
                        if target == '.' or get_color(target) != color:
                            print("Yes")
                            return

            # Король
            elif p_low == 'k':
                for dr, dc in directions['king']:
                    nr, nc = r + dr, c + dc
                    if inside(nr, nc):
                        target = board[nr][nc]
                        if target == '.' or get_color(target) != color:
                            print("Yes")
                            return

            # Ладья
            elif p_low == 'r':
                for dr, dc in directions['rook']:
                    nr, nc = r + dr, c + dc
                    while inside(nr, nc):
                        target = board[nr][nc]
                        if target == '.':
                            print("Yes")
                            return
                        if get_color(target) != color:
                            print("Yes")
                            return
                        # своя фигура – дальше не идём
                        break
                        # (теоретически сюда не попадём из-за return, но для ясности оставим)

            # Слон
            elif p_low == 'b':
                for dr, dc in directions['bishop']:
                    nr, nc = r + dr, c + dc
                    while inside(nr, nc):
                        target = board[nr][nc]
                        if target == '.':
                            print("Yes")
                            return
                        if get_color(target) != color:
                            print("Yes")
                            return
                        break

            # Ферзь
            elif p_low == 'q':
                for dr, dc in directions['queen']:
                    nr, nc = r + dr, c + dc
                    while inside(nr, nc):
                        target = board[nr][nc]
                        if target == '.':
                            print("Yes")
                            return
                        if get_color(target) != color:
                            print("Yes")
                            return
                        break

    # Если ни одна фигура не может сделать ход
    print("No")

if __name__ == "__main__":
    main()