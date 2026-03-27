using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Использование: dotnet run <файл> [-i]");
            Console.WriteLine("-i : игнорировать регистр");
            return;
        }

        string filePath = args[0];
        bool ignoreCase = args.Length > 1 && args[1] == "-i";

        try
        {
            string content = File.ReadAllText(filePath);
            var frequencies = CountFrequencies(content, ignoreCase);
            
            Console.WriteLine($"Частота символов{(ignoreCase ? " (регистр не учитывается)" : "")}:");
            Console.WriteLine("Символ | Частота | Процент");
            Console.WriteLine("-------|---------|--------");
            
            int total = frequencies.Values.Sum();
            
            foreach (var kv in frequencies)
            {
                string displayChar = kv.Key == ' ' ? "[пробел]" :
                                    kv.Key == '\n' ? "[\\n]" :
                                    kv.Key == '\r' ? "[\\r]" :
                                    kv.Key == '\t' ? "[табуляция]" : kv.Key.ToString();
                
                double percent = (double)kv.Value / total * 100;
                Console.WriteLine($"{displayChar,-7} | {kv.Value,-7} | {percent:F2}%");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка: {ex.Message}");
        }
    }

    static Dictionary<char, int> CountFrequencies(string text, bool ignoreCase)
    {
        var freq = new Dictionary<char, int>();
        
        foreach (char c in text)
        {
            char key = ignoreCase ? char.ToLower(c) : c;
            
            if (freq.ContainsKey(key))
                freq[key]++;
            else
                freq[key] = 1;
        }
        
        // Сортировка по убыванию частоты
        return freq.OrderByDescending(kv => kv.Value)
                   .ThenBy(kv => kv.Key)
                   .ToDictionary(kv => kv.Key, kv => kv.Value);
    }
}
