using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        Console.WriteLine("Анализ частоты символов в файле");
        Console.WriteLine("================================");
        
        Console.Write("Введите путь к файлу: ");
        string filePath = Console.ReadLine();

        if (!File.Exists(filePath))
        {
            Console.WriteLine("Файл не найден!");
            return;
        }

        try
        {
            string text = File.ReadAllText(filePath);

            Dictionary<char, int> frequencies = new Dictionary<char, int>();

            foreach (char c in text)
            {
                if (frequencies.ContainsKey(c))
                    frequencies[c]++;
                else
                    frequencies[c] = 1;
            }

            Console.WriteLine($"\nВсего символов: {text.Length}");
            Console.WriteLine("Результаты:");

            foreach (var item in frequencies)
            {
                if (item.Key != ' ' && item.Key != '\n' && item.Key != '\r' && item.Key != '\t')
                {
                    Console.WriteLine($"'{item.Key}': {item.Value} раз");
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка: {ex.Message}");
        }

        Console.WriteLine("\nНажмите любую клавишу для выхода...");
        Console.ReadKey();
    }
}