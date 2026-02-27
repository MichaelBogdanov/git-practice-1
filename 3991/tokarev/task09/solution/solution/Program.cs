using System;
using System.IO;
using System.Text;

class Program
{
    static void Main()
    {
        try
        {
            Console.WriteLine("Введите строку для сжатия (или путь к файлу):");
            string input = Console.ReadLine();

            string text;

            // Проверяем, является ли ввод путем к файлу
            if (File.Exists(input))
            {
                text = File.ReadAllText(input).Trim();
                Console.WriteLine($"\nПрочитано из файла: {text}");
            }
            else
            {
                text = input;
            }

            // Сжимаем строку
            string compressed = CompressRLE(text);

            Console.WriteLine($"\nИсходная строка: {text}");
            Console.WriteLine($"Сжатая строка: {compressed}");

            // Сохраняем в файл
            File.WriteAllText("compressed.txt", compressed);
            Console.WriteLine("\nРезультат сохранен в compressed.txt");

            // Показываем статистику сжатия
            double ratio = (double)compressed.Length / text.Length * 100;
            Console.WriteLine($"Коэффициент сжатия: {ratio:F1}%");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка: {ex.Message}");
        }
    }

    static string CompressRLE(string input)
    {
        if (string.IsNullOrEmpty(input))
            return "";

        StringBuilder result = new StringBuilder();
        int count = 1;
        char current = input[0];

        for (int i = 1; i < input.Length; i++)
        {
            if (input[i] == current)
            {
                count++;
            }
            else
            {
                result.Append(current);
                result.Append(count);
                current = input[i];
                count = 1;
            }
        }

        // Добавляем последний символ
        result.Append(current);
        result.Append(count);

        return result.ToString();
    }
}