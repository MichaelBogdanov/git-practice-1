using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите числа через пробел:");
        string[] parts = Console.ReadLine().Split();

        List<int> result = new List<int>();

        for (int i = 0; i < parts.Length; i++)
        {
            int num = int.Parse(parts[i]);

            bool exists = false;
            for (int j = 0; j < result.Count; j++)
            {
                if (result[j] == num)
                {
                    exists = true;
                    break;
                }
            }

            if (!exists)
            {
                result.Add(num);
            }
        }

        Console.WriteLine("Результат:");
        for (int i = 0; i < result.Count; i++)
        {
            Console.Write(result[i] + " ");
        }
        Console.WriteLine();
    }
}