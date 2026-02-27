using System;
using System.IO;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        try
        {
            string[] board = File.ReadAllLines("board.txt");

            Console.WriteLine("Текущая доска:");
            Console.WriteLine("  a b c d e f g h");
            Console.WriteLine("  ---------------");

            for (int i = 0; i < 8; i++)
            {
                Console.Write($"{8 - i} ");
                foreach (char c in board[i])
                {
                    Console.Write($"{c} ");
                }
                Console.WriteLine($" {8 - i}");
            }

            Console.WriteLine("  ---------------");
            Console.WriteLine("  a b c d e f g h");

            Console.WriteLine("\nВведите ход (формат: начальная_позиция конечная_позиция)");
            Console.WriteLine("Например: e2 e4");
            string move = Console.ReadLine();

            // Парсим ход
            string[] positions = move.ToLower().Split(' ');
            if (positions.Length != 2)
            {
                Console.WriteLine("Неверный формат хода!");
                return;
            }

            string from = positions[0];
            string to = positions[1];

            // Проверяем ход
            bool isValid = ValidateMove(board, from, to);

            Console.WriteLine("\n" + new string('=', 40));
            Console.WriteLine($"Ход: {from.ToUpper()} -> {to.ToUpper()}");
            Console.WriteLine($"Результат: {(isValid ? "РАЗРЕШЕН" : "ЗАПРЕЩЕН")}");
            Console.WriteLine(new string('=', 40));

            // Показываем фигуру, которой ходили
            (int x1, int y1) = ParsePosition(from);
            char piece = board[y1][x1];
            string pieceName = GetPieceName(piece);

            if (piece != '.')
            {
                Console.WriteLine($"Фигура: {pieceName} ({(char.IsUpper(piece) ? "белые" : "черные")})");
            }

            // Показываем целевую клетку
            (int x2, int y2) = ParsePosition(to);
            char targetPiece = board[y2][x2];

            if (targetPiece != '.')
            {
                string targetName = GetPieceName(targetPiece);
                Console.WriteLine($"Цель: {targetName} ({(char.IsUpper(targetPiece) ? "белые" : "черные")})");
            }

            Console.WriteLine(new string('=', 40));
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine("ОШИБКА: Файл board.txt не найден!");
            Console.WriteLine("\nСоздайте файл board.txt с начальной позицией:");
            Console.WriteLine("rnbqkbnr");
            Console.WriteLine("pppppppp");
            Console.WriteLine("........");
            Console.WriteLine("........");
            Console.WriteLine("........");
            Console.WriteLine("........");
            Console.WriteLine("PPPPPPPP");
            Console.WriteLine("RNBQKBNR");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка: {ex.Message}");
        }

        Console.WriteLine("\nНажмите любую клавишу для выхода...");
        Console.ReadKey();
    }

    static string GetPieceName(char piece)
    {
        return char.ToUpper(piece) switch
        {
            'K' => "Король",
            'Q' => "Ферзь",
            'R' => "Ладья",
            'B' => "Слон",
            'N' => "Конь",
            'P' => "Пешка",
            _ => "Неизвестная фигура"
        };
    }

    static bool ValidateMove(string[] board, string from, string to)
    {
        // Конвертируем координаты (например, "e2" -> (4, 6))
        (int x1, int y1) = ParsePosition(from);
        (int x2, int y2) = ParsePosition(to);

        // Проверяем, что позиции в пределах доски
        if (!IsValidPosition(x1, y1) || !IsValidPosition(x2, y2))
            return false;

        // Получаем фигуру
        char piece = board[y1][x1];

        // Проверяем, что есть фигура
        if (piece == '.')
            return false;

        // Проверяем, что не бьем свою фигуру
        char targetPiece = board[y2][x2];
        if (targetPiece != '.' && char.IsUpper(piece) == char.IsUpper(targetPiece))
            return false;

        // Проверяем ход в зависимости от типа фигуры
        bool isValid = piece.ToString().ToUpper() switch
        {
            "P" => ValidatePawn(piece, x1, y1, x2, y2, board),
            "R" => ValidateRook(x1, y1, x2, y2, board),
            "N" => ValidateKnight(x1, y1, x2, y2),
            "B" => ValidateBishop(x1, y1, x2, y2, board),
            "Q" => ValidateQueen(x1, y1, x2, y2, board),
            "K" => ValidateKing(x1, y1, x2, y2),
            _ => false
        };

        return isValid;
    }

    static (int, int) ParsePosition(string pos)
    {
        int x = pos[0] - 'a';  // 'a' -> 0, 'b' -> 1, etc.
        int y = 8 - (pos[1] - '0');  // '1' -> 7, '2' -> 6, etc.
        return (x, y);
    }

    static bool IsValidPosition(int x, int y)
    {
        return x >= 0 && x < 8 && y >= 0 && y < 8;
    }

    static bool ValidatePawn(char piece, int x1, int y1, int x2, int y2, string[] board)
    {
        int direction = char.IsUpper(piece) ? -1 : 1;  // Белые идут вверх (-1), черные вниз (+1)
        int startRow = char.IsUpper(piece) ? 6 : 1;    // Белые стартуют с 6 ряда, черные с 1

        // Обычный ход на 1 клетку вперед
        if (x1 == x2 && y2 == y1 + direction && board[y2][x2] == '.')
            return true;

        // Первый ход на 2 клетки
        if (x1 == x2 && y1 == startRow && y2 == y1 + 2 * direction &&
            board[y1 + direction][x1] == '.' && board[y2][x2] == '.')
            return true;

        // Взятие фигуры
        if (Math.Abs(x2 - x1) == 1 && y2 == y1 + direction && board[y2][x2] != '.')
            return true;

        return false;
    }

    static bool ValidateRook(int x1, int y1, int x2, int y2, string[] board)
    {
        if (x1 != x2 && y1 != y2)
            return false;

        // Проверяем, что путь свободен
        return IsPathClear(x1, y1, x2, y2, board);
    }

    static bool ValidateKnight(int x1, int y1, int x2, int y2)
    {
        int dx = Math.Abs(x2 - x1);
        int dy = Math.Abs(y2 - y1);
        return (dx == 2 && dy == 1) || (dx == 1 && dy == 2);
    }

    static bool ValidateBishop(int x1, int y1, int x2, int y2, string[] board)
    {
        if (Math.Abs(x2 - x1) != Math.Abs(y2 - y1))
            return false;

        return IsPathClear(x1, y1, x2, y2, board);
    }

    static bool ValidateQueen(int x1, int y1, int x2, int y2, string[] board)
    {
        // Ладья + слон
        if (x1 == x2 || y1 == y2 || Math.Abs(x2 - x1) == Math.Abs(y2 - y1))
            return IsPathClear(x1, y1, x2, y2, board);

        return false;
    }

    static bool ValidateKing(int x1, int y1, int x2, int y2)
    {
        return Math.Abs(x2 - x1) <= 1 && Math.Abs(y2 - y1) <= 1;
    }

    static bool IsPathClear(int x1, int y1, int x2, int y2, string[] board)
    {
        int dx = Math.Sign(x2 - x1);
        int dy = Math.Sign(y2 - y1);

        int x = x1 + dx;
        int y = y1 + dy;

        // Проверяем все клетки до конечной
        while (x != x2 || y != y2)
        {
            if (board[y][x] != '.')
                return false;

            x += dx;
            y += dy;
        }

        return true;
    }
}