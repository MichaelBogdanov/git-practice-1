using System;
using System.IO;

class Program
{
    static void Main()
    {


        File.WriteAllText("board.txt", "RNBQKBNR\r\nPPPPPPPP\r\n........\r\n........\r\n........\r\n........\r\npppppppp\r\nrnbqkbnr");

        string[] board = File.ReadAllLines("board.txt");

        Console.Write("Введите ход: ");
        string move = Console.ReadLine();

       
        string from = move.Split(' ')[0];
        string to = move.Split(' ')[1];

       
        int fromX = from[0] - 'a';
        int fromY = 8 - int.Parse(from[1].ToString());
        int toX = to[0] - 'a';
        int toY = 8 - int.Parse(to[1].ToString());

        char piece = board[fromY][fromX];

        if (piece == '.')
        {
            Console.WriteLine("INVALID");
            return;
        }

        char target = board[toY][toX];
        if (target != '.' && char.IsUpper(piece) == char.IsUpper(target))
        {
            Console.WriteLine("INVALID");
            return;
        }

        bool valid = false;

        switch (char.ToLower(piece))
        {
            case 'p': 
                int dir = char.IsUpper(piece) ? -1 : 1;
                if (fromX == toX && toY - fromY == dir && target == '.')
                    valid = true;
                if (fromX == toX && toY - fromY == 2 * dir &&
                    ((char.IsUpper(piece) && fromY == 6) || (!char.IsUpper(piece) && fromY == 1)) &&
                    target == '.')
                    valid = true;
                if (Math.Abs(toX - fromX) == 1 && toY - fromY == dir && target != '.')
                    valid = true;
                break;

            case 'n': 
                int dx = Math.Abs(toX - fromX);
                int dy = Math.Abs(toY - fromY);
                if ((dx == 2 && dy == 1) || (dx == 1 && dy == 2))
                    valid = true;
                break;

            case 'b': 
                if (Math.Abs(toX - fromX) == Math.Abs(toY - fromY))
                    valid = true;
                break;

            case 'r': 
                if (fromX == toX || fromY == toY)
                    valid = true;
                break;

            case 'q':
                if (fromX == toX || fromY == toY ||
                    Math.Abs(toX - fromX) == Math.Abs(toY - fromY))
                    valid = true;
                break;

            case 'k': 
                if (Math.Abs(toX - fromX) <= 1 && Math.Abs(toY - fromY) <= 1)
                    valid = true;
                break;
        }

    
        if (valid && (piece == 'B' || piece == 'b' || piece == 'R' || piece == 'r' ||
                      piece == 'Q' || piece == 'q'))
        {
            int stepX = toX > fromX ? 1 : (toX < fromX ? -1 : 0);
            int stepY = toY > fromY ? 1 : (toY < fromY ? -1 : 0);

            int x = fromX + stepX;
            int y = fromY + stepY;

            while (x != toX || y != toY)
            {
                if (board[y][x] != '.')
                {
                    valid = false;
                    break;
                }
                x += stepX;
                y += stepY;
            }
        }

        Console.WriteLine(valid ? "VALID" : "INVALID");
    }
}