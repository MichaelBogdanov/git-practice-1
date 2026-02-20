using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace task11
{

    // че за задание такое, ешки кошки

    class ChessMoveValidator
    {
        static void Main(string[] args)
        {
            string[] board = File.ReadAllLines("board.txt");

            string[] move = Console.ReadLine().Split();
            string from = move[0];
            string to = move[1];

            // конвертация координат (a1 -> (0,0))
            int fromX = from[0] - 'a';
            int fromY = 8 - (from[1] - '0');
            int toX = to[0] - 'a';
            int toY = 8 - (to[1] - '0');

            // вывод в консоль
            bool isValid = IsValidMove(board, fromX, fromY, toX, toY);
            Console.WriteLine(isValid ? "VALID" : "INVALID");
        }

        static bool IsValidMove(string[] board, int fromX, int fromY, int toX, int toY)
        {
            // проверка границ
            if (fromX < 0 || fromX >= 8 || fromY < 0 || fromY >= 8 ||
                toX < 0 || toX >= 8 || toY < 0 || toY >= 8)
                return false;

            char piece = board[fromY][fromX];
            char target = board[toY][toX];

            // нет фигуры на начальной позиции
            if (piece == '.') return false;

            // нельзя бить свою фигуру
            bool isWhite = char.IsUpper(piece);
            bool targetIsWhite = char.IsUpper(target);
            if (target != '.' && isWhite == targetIsWhite) return false;

            // проверка хода по типу фигуры (без рекурсивных шаблонов)
            char pieceType = char.ToLower(piece);
            bool valid = false;

            if (pieceType == 'p')
                valid = IsValidPawn(board, fromX, fromY, toX, toY, isWhite);
            else if (pieceType == 'n')
                valid = IsValidKnight(fromX, fromY, toX, toY);
            else if (pieceType == 'b')
                valid = IsValidBishop(board, fromX, fromY, toX, toY);
            else if (pieceType == 'r')
                valid = IsValidRook(board, fromX, fromY, toX, toY);
            else if (pieceType == 'q')
                valid = IsValidQueen(board, fromX, fromY, toX, toY);
            else if (pieceType == 'k')
                valid = IsValidKing(fromX, fromY, toX, toY);

            return valid;
        }

        static bool IsValidPawn(string[] board, int fromX, int fromY, int toX, int toY, bool isWhite)
        {
            int direction = isWhite ? -1 : 1;
            int startRow = isWhite ? 6 : 1;

            // обычный ход вперед
            if (fromX == toX && toY == fromY + direction && board[toY][toX] == '.')
                return true;

            // первый ход на 2 клетки
            if (fromX == toX && fromY == startRow && toY == fromY + 2 * direction &&
                board[fromY + direction][fromX] == '.' && board[toY][toX] == '.')
                return true;

            // взятие
            if (Math.Abs(toX - fromX) == 1 && toY == fromY + direction && board[toY][toX] != '.')
                return true;

            return false;
        }

        // метод под кужду фигуру
        static bool IsValidKnight(int fromX, int fromY, int toX, int toY)
        {
            int dx = Math.Abs(toX - fromX);
            int dy = Math.Abs(toY - fromY);
            return (dx == 2 && dy == 1) || (dx == 1 && dy == 2);
        }

        static bool IsValidBishop(string[] board, int fromX, int fromY, int toX, int toY)
        {
            if (Math.Abs(toX - fromX) != Math.Abs(toY - fromY)) return false;
            return IsPathClear(board, fromX, fromY, toX, toY);
        }

        static bool IsValidRook(string[] board, int fromX, int fromY, int toX, int toY)
        {
            if (fromX != toX && fromY != toY) return false;
            return IsPathClear(board, fromX, fromY, toX, toY);
        }

        static bool IsValidQueen(string[] board, int fromX, int fromY, int toX, int toY)
        {
            if (fromX != toX && fromY != toY && Math.Abs(toX - fromX) != Math.Abs(toY - fromY))
                return false;
            return IsPathClear(board, fromX, fromY, toX, toY);
        }

        static bool IsValidKing(int fromX, int fromY, int toX, int toY)
        {
            return Math.Abs(toX - fromX) <= 1 && Math.Abs(toY - fromY) <= 1;
        }

        static bool IsPathClear(string[] board, int fromX, int fromY, int toX, int toY)
        {
            int stepX = toX == fromX ? 0 : (toX > fromX ? 1 : -1);
            int stepY = toY == fromY ? 0 : (toY > fromY ? 1 : -1);

            int x = fromX + stepX;
            int y = fromY + stepY;

            while (x != toX || y != toY)
            {
                if (board[y][x] != '.') return false;
                x += stepX;
                y += stepY;
            }

            return true;
        }
    }
}
