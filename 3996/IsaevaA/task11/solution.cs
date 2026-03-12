using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите начальную клетку (например, a1):");
        string from = Console.ReadLine();

        Console.WriteLine("Введите конечную клетку (например, h8):");
        string to = Console.ReadLine();

        int x1 = from[0] - 'a' + 1;
        int y1 = int.Parse(from[1].ToString());

        int x2 = to[0] - 'a' + 1;
        int y2 = int.Parse(to[1].ToString());

        if (x1 == x2 || y1 == y2 || Math.Abs(x1 - x2) == Math.Abs(y1 - y2))
        {
            Console.WriteLine("Ход возможен");
        }
        else
        {
            Console.WriteLine("Ход невозможен");
        }
    }
}