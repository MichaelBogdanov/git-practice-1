# Загрузка доски из файла board.txt
def load_board(filename):
    with open(filename, 'r') as f:
        return [list(f.readline().strip()) for _ in range(8)]  # создаем список списков (матрицу 8x8)

# Вывод доски в удобоном виде с координатами
def print_board(board):
    print("  a b c d e f g h")
    for i in range(8):
        row = board[i]
        print(8-i, end=" ")
        for cell in row:
            print(cell, end=" ")  
        print(8-i)
    print("  a b c d e f g h\n")

# Проверка, находится ли координата внутри доски
def inside(x, y):
    return 0 <= x < 8 and 0 <= y < 8

# Проверка цвета фигуры
# Заглавные буквы - белые
# Строчные буквы - черные
def is_white(c):
    return c.isupper()

def is_black(c):
    return c.islower()  

# Проверка, свободен ли путь для фигур, которые ходят по прямой или диагонали
# Используется для ладьи, слона, ферзя
def path_clear(board, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    step_x = 0 if dx == 0 else dx // abs(dx)
    step_y = 0 if dy == 0 else dy // abs(dy)  
    x, y = x1 + step_x, y1 + step_y
    while (x, y) != (x2, y2):
        if board[x][y] != '.':  # если на пути есть фигура, движение невозможно
            return False
        x += step_x
        y += step_y
    return True

# Основная функция проверки корректности хода
def valid_move(board, x1, y1, x2, y2):
    # Проверка, что обе клетки находятся внутри доски
    if not inside(x1, y1) or not inside(x2, y2):
        return False

    piece = board[x1][y1]  # фигура, которую хотим передвинуть
    if piece == '.':  # пустую клетку передвигать нельзя
        return False

    target = board[x2][y2]  # клетка назначения

    # Нельзя бить свою фигуру
    if (is_white(piece) and is_white(target)) or (is_black(piece) and is_black(target)):
        return False

    dx = x2 - x1  # вертикальная разница
    dy = y2 - y1  # горизонтальная разница
    piece_type = piece.upper()

    # Пешка 
    if piece_type == 'P':
        direction = -1 if is_white(piece) else 1  # белые ходят вверх по доске, черные вниз
        start_row = 6 if is_white(piece) else 1  # начальная позиция пешки

        # Ход на 1 клетку вперед
        if dy == 0 and dx == direction and target == '.':
            return True

        # Ход на 2 клетки со стартовой позиции
        if dy == 0 and dx == 2*direction and x1 == start_row and board[x1 + direction][y1] == '.' and target == '.':
            return True

        # Взятие по диагонали
        if abs(dy) == 1 and dx == direction and target != '.':
            return True

        return False
  


    # Ладья
    if piece_type == 'R':
        if dx == 0 or dy == 0:  # движение по вертикали или горизонтали
            return path_clear(board, x1, y1, x2, y2)
        return False

    # Слон 
    if piece_type == 'B':
        if abs(dx) == abs(dy):  # движение по диагонали
            return path_clear(board, x1, y1, x2, y2)
        return False

    # Ферзь 
    if piece_type == 'Q':
        if dx == 0 or dy == 0 or abs(dx) == abs(dy):  # вертикаль, горизонталь или диагональ
            return path_clear(board, x1, y1, x2, y2)
        return False

    # Король
    if piece_type == 'K':
        return abs(dx) <= 1 and abs(dy) <= 1  # король ходит на одну клетку в любом направлении

    # Конь
    if piece_type == 'N':
        # Г-образный ход: 2+1 клетки
        return (abs(dx) == 2 and abs(dy) == 1) or (abs(dx) == 1 and abs(dy) == 2)

    return False

board = load_board("board.txt")

# Вывод доски в консоль
print("Текущая доска:")
print_board(board)

# Ввод хода
move_from = input("Введите ход: ")
move_to = input("Введите куда: ")

# Перевод координат из шахматной записи в индексы массива
y1 = ord(move_from[0]) - oиrd('a')  # столбец 0-7
x1 = 8 - int(move_from[1])         # строка 0-7
y2 = ord(move_to[0]) - ord('a')
x2 = 8 - int(move_to[1])

# Проверка, можно ли сделать ход
if valid_move(board, x1, y1, x2, y2):
    print("YES")
else:
    print("NO")