using System.Diagnostics.CodeAnalysis;

namespace RLEcompression
{
    class Program
    {
        static void Main(string[] args)
        {
            Menu();
        }
        static void RLECompression(string inputString)
        {
            var pairs = new List<Tuple<char, int>>();

            int count = 1;
            for (int i = 0; i < inputString.Length; i++)
            {
                if (i < inputString.Length - 1 && inputString[i] == inputString[i + 1])
                {
                    count++;
                }
                else
                {
                    pairs.Add(Tuple.Create(inputString[i], count));
                    count = 1;
                }
            }

            string result = "";
            foreach (var pair in pairs)
            {
                result += pair.Item1;
                result += pair.Item2;
            }
            Console.WriteLine(result);
        }
        static void RLEDecompression(string compString)
        {
            string result = "";

            for (int i = 0; i < compString.Length; i++)
            {
                if (char.IsLetter(compString[i]))
                {
                    char symbol = compString[i];
                    string numStr = "";

                    int j = i + 1;
                    while (j < compString.Length && char.IsDigit(compString[j]))
                    {
                        numStr += compString[j];
                        j++;
                    }

                    int count = int.Parse(numStr);
                    for (int k = 0; k < count; k++)
                    {
                        result += symbol;
                    }

                    i = j - 1;
                }
            }

            Console.WriteLine(result);
        }
        static void Menu()
        {
            Console.WriteLine("1. Компрессия");
            Console.WriteLine("2. Декомпрессия");
            int answer = Convert.ToInt32(Console.ReadLine());

            switch (answer)
            {
                case 1:
                    Console.WriteLine("Введите строку для компрессии: ");
                    string compString = Console.ReadLine();
                    RLECompression(compString);
                    break;
                case 2:
                    Console.WriteLine("Введите строку для декомпрессии: ");
                    string decompString = Console.ReadLine();
                    RLEDecompression(decompString);
                    break;
                default:
                    Console.WriteLine("Не верный пункт");
                    break;

            }
        }
    }
}