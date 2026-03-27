using System;
using System.IO;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length < 2)
        {
            Console.WriteLine("Использование: dotnet run <файл> <алгоритм>");
            Console.WriteLine("Алгоритмы: merge, quick, bubble");
            return;
        }

        string filePath = args[0];
        string algorithm = args[1].ToLower();

        string content = File.ReadAllText(filePath);
        int[] numbers = content.Split(new[] { ' ', '\n', '\r', '\t' }, 
                                      StringSplitOptions.RemoveEmptyEntries)
                              .Select(int.Parse)
                              .ToArray();

        Console.WriteLine($"Исходный массив: [{string.Join(", ", numbers)}]");

        int[] sorted = null;

        switch (algorithm)
        {
            case "merge":
                sorted = MergeSort(numbers);
                Console.WriteLine("Сортировка слиянием (Merge Sort)");
                break;
            case "quick":
                sorted = QuickSort(numbers);
                Console.WriteLine("Быстрая сортировка (Quick Sort)");
                break;
            case "bubble":
                sorted = BubbleSort(numbers);
                Console.WriteLine("Пузырьковая сортировка (Bubble Sort)");
                break;
            default:
                Console.WriteLine("Используйте: merge, quick или bubble");
                return;
        }

        Console.WriteLine($"Отсортированный массив: [{string.Join(", ", sorted)}]");
        File.WriteAllText("output.txt", string.Join(" ", sorted));
        Console.WriteLine("Результат сохранен в output.txt");
    }

    static int[] MergeSort(int[] array)
    {
        if (array.Length <= 1) return array;
        
        int mid = array.Length / 2;
        int[] left = new int[mid];
        int[] right = new int[array.Length - mid];
        
        Array.Copy(array, 0, left, 0, mid);
        Array.Copy(array, mid, right, 0, array.Length - mid);
        
        return Merge(MergeSort(left), MergeSort(right));
    }

    static int[] Merge(int[] left, int[] right)
    {
        int[] result = new int[left.Length + right.Length];
        int i = 0, j = 0, k = 0;
        
        while (i < left.Length && j < right.Length)
        {
            if (left[i] <= right[j])
                result[k++] = left[i++];
            else
                result[k++] = right[j++];
        }
        
        while (i < left.Length) result[k++] = left[i++];
        while (j < right.Length) result[k++] = right[j++];
        
        return result;
    }

    static int[] QuickSort(int[] array)
    {
        int[] result = (int[])array.Clone();
        QuickSortRecursive(result, 0, result.Length - 1);
        return result;
    }

    static void QuickSortRecursive(int[] array, int left, int right)
    {
        if (left >= right) return;
        int pivot = Partition(array, left, right);
        QuickSortRecursive(array, left, pivot - 1);
        QuickSortRecursive(array, pivot + 1, right);
    }

    static int Partition(int[] array, int left, int right)
    {
        int pivot = array[right];
        int i = left - 1;
        
        for (int j = left; j < right; j++)
        {
            if (array[j] <= pivot)
            {
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        
        int temp2 = array[i + 1];
        array[i + 1] = array[right];
        array[right] = temp2;
        
        return i + 1;
    }

    static int[] BubbleSort(int[] array)
    {
        int[] result = (int[])array.Clone();
        for (int i = 0; i < result.Length - 1; i++)
        {
            for (int j = 0; j < result.Length - i - 1; j++)
            {
                if (result[j] > result[j + 1])
                {
                    int temp = result[j];
                    result[j] = result[j + 1];
                    result[j + 1] = temp;
                }
            }
        }
        return result;
    }
}
