using System;
using System.Linq;

namespace WordReverser
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.InputEncoding = System.Text.Encoding.UTF8;

            Console.WriteLine("Введите текст:");
            string input = Console.ReadLine();

            if (string.IsNullOrWhiteSpace(input))
            {
                Console.WriteLine("Пустая строка.");
            }
            else
            {
                string[] words = input.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

                Array.Reverse(words);

                string result = string.Join(" ", words);

                Console.WriteLine("\nРезультат:");
                Console.WriteLine(result);
            }

            Console.ReadKey();
        }
    }
}
