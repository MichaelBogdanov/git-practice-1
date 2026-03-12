using System;
using System.IO;
using System.Text;
using System.Collections.Generic;


public class Program
{
    private static readonly string Lower = "abcdefghijklmnopqrstuvwxyz";
    private static readonly string Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static readonly string Digits = "0123456789";
    private static readonly string Special = "!@#$%^&*()_+-=[]{}|;:,.<>?";

    public static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.Error.WriteLine("Ошибка: Не указан путь к файлу.");
            Console.Error.WriteLine("Использование: solution.exe <путь_к_файлу>");
            return;
        }

        string filePath = args[0];

        if (!File.Exists(filePath))
        {
            Console.Error.WriteLine($"Ошибка: Файл '{filePath}' не найден.");
            return;
        }

        try
        {
            using (var reader = new StreamReader(filePath))
            {
                Solve(reader);
            }
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine($"Ошибка при чтении файла: {ex.Message}");
        }
    }

    private static void Solve(TextReader input)
    {
        string? lenStr = input.ReadLine();
        if (!int.TryParse(lenStr, out int length) || length <= 0)
        {
            Console.Error.WriteLine("Ошибка: Неверная длина пароля.");
            return;
        }

        bool useDigits = ParseBool(input.ReadLine());
        bool useUpper = ParseBool(input.ReadLine());
        bool useLower = ParseBool(input.ReadLine());
        bool useSpecial = ParseBool(input.ReadLine());

        if (!useDigits && !useUpper && !useLower && !useSpecial)
        {
            useDigits = useUpper = useLower = useSpecial = true;
        }

        string password = GeneratePassword(length, useDigits, useUpper, useLower, useSpecial);
        
        if (!string.IsNullOrEmpty(password))
        {
            Console.WriteLine(password);
        }
    }

    private static bool ParseBool(string? value)
    {
        if (string.IsNullOrEmpty(value))
            return false;
        return value.ToLower() == "true" || value == "1" || value.ToLower() == "да";
    }

    private static string GeneratePassword(int length, bool digits, bool upper, bool lower, bool special)
    {
        var charSets = new List<string>();
        var requiredChars = new List<char>();
        Random rnd = new Random();

        if (lower) 
        { 
            charSets.Add(Lower); 
            requiredChars.Add(Lower[rnd.Next(Lower.Length)]); 
        }
        if (upper) 
        { 
            charSets.Add(Upper); 
            requiredChars.Add(Upper[rnd.Next(Upper.Length)]); 
        }
        if (digits) 
        { 
            charSets.Add(Digits); 
            requiredChars.Add(Digits[rnd.Next(Digits.Length)]); 
        }
        if (special) 
        { 
            charSets.Add(Special); 
            requiredChars.Add(Special[rnd.Next(Special.Length)]); 
        }

        int requiredCount = requiredChars.Count;

        if (length < requiredCount)
        {
            Console.Error.WriteLine($"Ошибка: Длина пароля ({length}) меньше количества обязательных наборов ({requiredCount}).");
            return "";
        }

        var passwordChars = new List<char>(requiredChars);

        var allChars = new StringBuilder();
        foreach (var set in charSets)
        {
            allChars.Append(set);
        }

        for (int i = 0; i < length - requiredCount; i++)
        {
            passwordChars.Add(allChars[rnd.Next(allChars.Length)]);
        }

        for (int i = passwordChars.Count - 1; i > 0; i--)
        {
            int j = rnd.Next(i + 1);
            char temp = passwordChars[i];
            passwordChars[i] = passwordChars[j];
            passwordChars[j] = temp;
        }

        return new string(passwordChars.ToArray());
    }
}