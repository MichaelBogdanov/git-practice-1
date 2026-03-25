using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main()
    {
        Console.Write("Длина пароля: ");
        int len = int.Parse(Console.ReadLine());

        Console.Write("Цифры? (y/n): ");
        bool d = Console.ReadLine().ToLower() == "y";

        Console.Write("Заглавные? (y/n): ");
        bool u = Console.ReadLine().ToLower() == "y";

        Console.Write("Строчные? (y/n): ");
        bool l = Console.ReadLine().ToLower() == "y";

        Console.Write("Спецсимволы? (y/n): ");
        bool s = Console.ReadLine().ToLower() == "y";

        Console.WriteLine($"Пароль: {GeneratePassword(len, d, u, l, s)}");
    }

    static string GeneratePassword(int len, bool d, bool u, bool l, bool s)
    {
        string digits = "0123456789";
        string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string lower = "abcdefghijklmnopqrstuvwxyz";
        string special = "!@#$%^&*()";

        string all = "";
        List<char> password = new List<char>();
        Random rnd = new Random();

        if (d) { all += digits; password.Add(digits[rnd.Next(digits.Length)]); }
        if (u) { all += upper; password.Add(upper[rnd.Next(upper.Length)]); }
        if (l) { all += lower; password.Add(lower[rnd.Next(lower.Length)]); }
        if (s) { all += special; password.Add(special[rnd.Next(special.Length)]); }

        while (password.Count < len)
            password.Add(all[rnd.Next(all.Length)]);

        return new string(password.OrderBy(x => rnd.Next()).ToArray());
    }
}