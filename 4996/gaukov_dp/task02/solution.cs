using System;
using System.IO;
using System.Collections.Generic;

/// <summary>
/// Задача 02: Подсчёт строк, слов и поиск самого длинного слова.
/// </summary>
public class Program
{
    public static void Main(string[] args)
    {
        // Проверяем, передан ли файл в качестве аргумента
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
        var lines = new List<string>();
        string? line;
        
        // Читаем все строки из файла
        while ((line = input.ReadLine()) != null)
        {
            lines.Add(line);
        }

        int lineCount = lines.Count;
        int wordCount = 0;
        string longestWord = "";
        
        // Разделители: пробельные символы и знаки пунктуации
        char[] separators = new char[] 
        { 
            ' ', '\t', '\n', '\r', 
            ',', '.', '!', '?', ';', ':', '-', 
            '(', ')', '[', ']', '{', '}', 
            '"', '\'', '<', '>', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '_', '+', '=' 
        };

        foreach (var textLine in lines)
        {
            // Разбиваем строку на слова, удаляя пустые элементы
            var words = textLine.Split(separators, StringSplitOptions.RemoveEmptyEntries);

            foreach (var word in words)
            {
                wordCount++;
                
                // Проверяем, является ли слово самым длинным
                if (word.Length > longestWord.Length)
                {
                    longestWord = word;
                }
            }
        }

        // Вывод результатов
        Console.WriteLine($"Строк: {lineCount}");
        Console.WriteLine($"Слов: {wordCount}");
        
        if (!string.IsNullOrEmpty(longestWord))
        {
            Console.WriteLine($"Самое длинное слово: {longestWord}");
            Console.WriteLine($"Длина самого длинного слова: {longestWord.Length}");
        }
        else
        {
            Console.WriteLine("Самое длинное слово: (не найдено)");
            Console.WriteLine("Длина самого длинного слова: 0");
        }
    }
}