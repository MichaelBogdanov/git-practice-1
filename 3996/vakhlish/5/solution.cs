using System;
using System.Text.RegularExpressions;

class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.InputEncoding = System.Text.Encoding.UTF8;
        Console.Write("Введите арабское или римское число (1-3999): ");
        string input = Console.ReadLine().ToUpper();
        if (int.TryParse(input, out int num) && num > 0 && num < 4000)
            Console.WriteLine($"Римское: {ToRoman(num)}");
        else if (Regex.IsMatch(input, "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$") && input != "")
            Console.WriteLine($"Арабское: {FromRoman(input)}");
        else
            Console.WriteLine("Ошибка: некорректный ввод или число вне диапазона");
    }

    static string ToRoman(int n)
    {
        int[] values = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        string[] RomanMap = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        string res = "";
        for (int i = 0; i < values.Length; i++)
            while (n >= values[i]) { res += RomanMap[i]; n -= values[i]; }
        return res;
    }

    static int FromRoman(string s)
    {
        int res = 0;
        for (int i = 0; i < s.Length; i++)
        {
            int cur = Val(s[i]), next = i + 1 < s.Length ? Val(s[i+1]) : 0;
            res += cur < next ? -cur : cur;
        }
        return res;
    }

    static int Val(char c) => c switch {'I'=>1, 'V'=>5, 'X'=>10, 'L'=>50, 'C'=>100, 'D'=>500, 'M'=>1000, _=>0};
}

