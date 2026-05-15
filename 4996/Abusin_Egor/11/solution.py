# Задача 11: Проверка шахматного хода

def read_board_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            board = []
            for line in file:
                line = line.strip()
                if line and len(line) == 8:
                    board.append(line)
            return board if len(board) == 8 else None
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
        return None

def get_piece_type(piece):
    if piece == '.':
        return None
    return piece.lower()

def get_piece_color(piece):
    if piece == '.':
        return None
    return 'white' if piece.isupper() else 'black'

def is_valid_move(board, from_row, from_col, to_row, to_col):
    piece = board[from_row][from_col]
    if piece == '.':
        return False
    
    target = board[to_row][to_col]
    piece_color = get_piece_color(piece)
    target_color = get_piece_color(target)
    
    if target_color == piece_color:
        return False
    
    piece_type = get_piece_type(piece)
    dr = to_row - from_row
    dc = to_col - from_col
    abs_dr = abs(dr)
    abs_dc = abs(dc)
    
    if piece_type == 'p':  # Пешка
        if piece_color == 'white':
            if dr == -1 and dc == 0 and target == '.':
                return True
            if dr == -1 and abs_dc == 1 and target != '.':
                return True
        else:  # black
            if dr == 1 and dc == 0 and target == '.':
                return True
            if dr == 1 and abs_dc == 1 and target != '.':
                return True
        return False
    
    elif piece_type == 'r':  # Ладья
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            for c in range(from_col + step, to_col, step):
                if board[from_row][c] != '.':
                    return False
            return True
        elif from_col == to_col:
            step = 1 if to_row > from_row else -1
            for r in range(from_row + step, to_row, step):
                if board[r][from_col] != '.':
                    return False
            return True
        return False
    
    elif piece_type == 'n':  # Конь
        return (abs_dr == 2 and abs_dc == 1) or (abs_dr == 1 and abs_dc == 2)
    
    elif piece_type == 'b':  # Слон
        if abs_dr == abs_dc:
            step_r = 1 if dr > 0 else -1
            step_c = 1 if dc > 0 else -1
            r, c = from_row + step_r, from_col + step_c
            while r != to_row:
                if board[r][c] != '.':
                    return False
                r += step_r
                c += step_c
            return True
        return False
    
    elif piece_type == 'q':  # Ферзь
        if from_row == to_row or from_col == to_col:
            return is_valid_move(board, from_row, from_col, to_row, to_col)
        elif abs_dr == abs_dc:
            return is_valid_move(board, from_row, from_col, to_row, to_col)
        return False
    
    elif piece_type == 'k':  # Король
        return max(abs_dr, abs_dc) == 1
    
    return False

print("=" * 50)
print("Задача 11: Проверка шахматного хода")
print("=" * 50)

filename = input("Введите имя файла с шахматной доской: ").strip()
board = read_board_from_file(filename)

if board:
    print("\nШахматная доска:")
    for row in board:
        print(row)
    
    try:
        print("\nВведите ход (пример: e2 e4)")
        move = input("> ").strip()
        from_pos, to_pos = move.split()
        
        from_col = ord(from_pos[0]) - ord('a')
        from_row = 8 - int(from_pos[1])
        to_col = ord(to_pos[0]) - ord('a')
        to_row = 8 - int(to_pos[1])
        
        if is_valid_move(board, from_row, from_col, to_row, to_col):
            print("VALID")
        else:
            print("INVALID")
    except:
        print("Ошибка: неверный формат хода")