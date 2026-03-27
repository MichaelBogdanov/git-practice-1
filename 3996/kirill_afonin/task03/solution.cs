using System;

class Program
{
    static string ReverseWords(string text)
    {
        string[] words = text.Split(' ');
        for (int i = 0; i < words.Length; i++)
        {
            char[] chars = words[i].ToCharArray();
            Array.Reverse(chars);
            words[i] = new string(chars);
        }
        return string.Join(" ", words);
    }

    static void Main()
    {
        Console.Write("Введите текст: ");
        string input = Console.ReadLine();
        string result = ReverseWords(input);
        Console.WriteLine("Результат: " + result);
    }
}