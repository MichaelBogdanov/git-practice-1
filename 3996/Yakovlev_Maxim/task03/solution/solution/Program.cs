using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        string inputFilePath = "input.txt";
        string outputFilePath = "output.txt";

        
        if (!File.Exists(inputFilePath))
        {
            Console.WriteLine($"Файл {inputFilePath} не найден.");
            return;
        }

        string text;

        text = File.ReadAllText(inputFilePath);

        string reversedText = ReverseWordsSimple(text);

            File.WriteAllText(outputFilePath, reversedText);
            Console.WriteLine("Текст успешно обработан и сохранен в файл output.txt");
      
    }

    static string ReverseWordsSimple(string text)
    {
        if (string.IsNullOrWhiteSpace(text))
            return string.Empty;

        
        text = text.Trim();

        
        string[] words = text.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

        
        Array.Reverse(words);

        
        return string.Join(" ", words);
    }
}