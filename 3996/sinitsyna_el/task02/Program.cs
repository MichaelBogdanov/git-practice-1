using System;
using System.IO;
using System.Text.RegularExpressions;
using System.Linq;
using System.Collections.Generic;

namespace WordCounter
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Укажите путь к файлу: dotnet run test.txt");
                return;
            }

            try
            {
                string content = File.ReadAllText(args[0]);
                var result = AnalyzeText(content);
                
                Console.WriteLine($"Количество строк: {result.LineCount}");
                Console.WriteLine($"Количество слов: {result.WordCount}");
                Console.WriteLine($"Самое длинное слово: \"{result.LongestWord}\" (длина: {result.LongestWordLength})");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка: {ex.Message}");
            }
        }

        static TextResult AnalyzeText(string text)
        {
            int lineCount = text.Split('\n').Length;
            
            var words = Regex.Matches(text, @"\b[\w']+\b")
                             .Cast<Match>()
                             .Select(m => m.Value)
                             .ToList();
            
            int wordCount = words.Count;
            
            string longestWord = "";
            int longestWordLength = 0;
            
            foreach (var word in words)
            {
                if (word.Length > longestWordLength)
                {
                    longestWordLength = word.Length;
                    longestWord = word;
                }
            }
            
            return new TextResult
            {
                LineCount = lineCount,
                WordCount = wordCount,
                LongestWord = longestWord,
                LongestWordLength = longestWordLength
            };
        }
    }

    class TextResult
    {
        public int LineCount { get; set; }
        public int WordCount { get; set; }
        public string LongestWord { get; set; }
        public int LongestWordLength { get; set; }
    }
}
