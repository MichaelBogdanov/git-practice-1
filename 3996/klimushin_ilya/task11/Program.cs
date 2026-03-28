using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length < 5)
        {
            Console.WriteLine("Использование: dotnet run board.txt x1 y1 x2 y2");
            return;
        }

        string[] board = File.ReadAllLines(args[0]);
        int x1 = int.Parse(args[1]);
        int y1 = int.Parse(args[2]);
        int x2 = int.Parse(args[3]);
        int y2 = int.Parse(args[4]);

        char piece = board[y1][x1];
        char target = board[y2][x2];

        if (piece == '.')
        {
            Console.WriteLine("NO");
            return;
        }

        bool canMove = false;

        switch (char.ToLower(piece))
        {
            case 'p':
                int dir = char.IsUpper(piece) ? -1 : 1;
                if (x1 == x2 && y2 == y1 + dir && target == '.')
                    canMove = true;
                if (Math.Abs(x2 - x1) == 1 && y2 == y1 + dir && target != '.' && char.IsUpper(piece) != char.IsUpper(target))
                    canMove = true;
                break;

            case 'n':
                int dx = Math.Abs(x2 - x1);
                int dy = Math.Abs(y2 - y1);
                canMove = (dx == 2 && dy == 1) || (dx == 1 && dy == 2);
                break;

            case 'r':
                if (x1 == x2 || y1 == y2)
                    canMove = IsClear(board, x1, y1, x2, y2);
                break;

            case 'b':
                if (Math.Abs(x2 - x1) == Math.Abs(y2 - y1))
                    canMove = IsClear(board, x1, y1, x2, y2);
                break;

            case 'q':
                if ((x1 == x2 || y1 == y2) || Math.Abs(x2 - x1) == Math.Abs(y2 - y1))
                    canMove = IsClear(board, x1, y1, x2, y2);
                break;

            case 'k':
                canMove = Math.Max(Math.Abs(x2 - x1), Math.Abs(y2 - y1)) == 1;
                break;
        }

        if (canMove && target != '.' && char.IsUpper(piece) == char.IsUpper(target))
            canMove = false;

        Console.WriteLine(canMove ? "YES" : "NO");
    }

    static bool IsClear(string[] board, int x1, int y1, int x2, int y2)
    {
        int dx = Math.Sign(x2 - x1);
        int dy = Math.Sign(y2 - y1);
        int x = x1 + dx;
        int y = y1 + dy;

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
