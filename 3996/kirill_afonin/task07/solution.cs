using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static Dictionary<char, int> CharFrequency(string text)
    {
        Dictionary<char, int> freq = new Dictionary<char, int>();
        
        foreach (char c in text)
        {
            if (freq.ContainsKey(c))
                freq[c]++;
            else
                freq[c] = 1;
        }
        
        return freq;
    }

    static void Main()
    {
        Console.Write("Введите строку: ");
        string input = Console.ReadLine();
        
        var freq = CharFrequency(input);
        
        Console.WriteLine("Частота символов:");
        foreach (var pair in freq.OrderBy(x => x.Key))
        {
            Console.WriteLine($"'{pair.Key}': {pair.Value}");
        }
    }
}