using System;
using System.IO;
using System.Collections.Generic;


public class Program
{
    public static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.Error.WriteLine("Ошибка: Не указан путь к файлу.");
            Console.Error.WriteLine("Использование: solution.exe <путь_к_файлу>");
            return;
        }

        string filePath = args[0];

        if (!File.Exists(filePath))
        {
            Console.Error.WriteLine($"Ошибка: Файл '{filePath}' не найден.");
            return;
        }

        try
        {
            using (var reader = new StreamReader(filePath))
            {
                Solve(reader);
            }
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine($"Ошибка при чтении файла: {ex.Message}");
        }
    }

    private static void Solve(TextReader input)
    {
        var numbers = new List<int>();
        string? line;
        
        while ((line = input.ReadLine()) != null)
        {
            var parts = line.Split(new char[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
            foreach (var part in parts)
            {
                if (int.TryParse(part, out int num))
                {
                    numbers.Add(num);
                }
            }
        }

        if (numbers.Count == 0)
        {
            Console.WriteLine("Массив пуст.");
            return;
        }

        int[] arr = numbers.ToArray();
        
        QuickSort(arr, 0, arr.Length - 1);

        Console.WriteLine(string.Join(" ", arr));
    }

   
    private static void QuickSort(int[] arr, int low, int high)
    {
        if (low < high)
        {
            int pi = Partition(arr, low, high);
            
            QuickSort(arr, low, pi - 1);
            QuickSort(arr, pi + 1, high);
        }
    }

  
    private static int Partition(int[] arr, int low, int high)
    {
        int pivot = arr[high];
        
        int i = (low - 1);

        for (int j = low; j < high; j++)
        {
            if (arr[j] <= pivot)
            {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp2 = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp2;

        return i + 1;
    }
}