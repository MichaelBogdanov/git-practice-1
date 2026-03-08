using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите ход (Пример: N b1 c3):");
        string input = Console.ReadLine();

        if (string.IsNullOrWhiteSpace(input)) return;

        try
        {
            string[] parts = input.Split(' ');
            if (parts.Length < 3) return;

            char piece = char.ToUpper(parts[0][0]);
            string from = parts[1].ToLower();
            string to = parts[2].ToLower();

            int x1 = from[0] - 'a';
            int y1 = from[1] - '1';
            int x2 = to[0] - 'a';
            int y2 = to[1] - '1';

            int dx = Math.Abs(x1 - x2);
            int dy = Math.Abs(y1 - y2);

            bool isValid = false;

            switch (piece)
            {
                case 'N': // Конь
                    isValid = (dx == 1 && dy == 2) || (dx == 2 && dy == 1);
                    break;
                case 'R': // Ладья
                    isValid = (dx == 0 || dy == 0);
                    break;
                case 'B': // Слон
                    isValid = (dx == dy);
                    break;
                case 'Q': // Ферзь
                    isValid = (dx == 0 || dy == 0 || dx == dy);
                    break;
                case 'K': // Король
                    isValid = (dx <= 1 && dy <= 1);
                    break;
            }

            Console.WriteLine(isValid ? "VALID" : "INVALID");
        }
        catch
        {
            Console.WriteLine("INVALID (ошибка ввода)");
        }
    }
}
