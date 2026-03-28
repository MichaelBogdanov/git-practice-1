using System;
using System.IO;
using System.Text.RegularExpressions;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        string text = File.ReadAllText(args[0]);
        
        int lines = text.Split('\n').Length;
        
        var words = Regex.Matches(text, @"\b[\w']+\b")
                         .Cast<Match>()
                         .Select(m => m.Value)
                         .ToList();
        
        int wordCount = words.Count;
        
        string longestWord = "";
        foreach (string w in words)
        {
            if (w.Length > longestWord.Length)
                longestWord = w;
        }
        
        Console.WriteLine($"Количество строк: {lines}");
        Console.WriteLine($"Количество слов: {wordCount}");
        Console.WriteLine($"Самое длинное слово: {longestWord} (длина: {longestWord.Length})");
    }
}
