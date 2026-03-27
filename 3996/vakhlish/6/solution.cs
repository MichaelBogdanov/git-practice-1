using System;

class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;

        int[] numbers = { 34, 7, 23, 32, 5, 62, 32, 2, 8, 1 };

        Console.WriteLine("Исходный массив:");
        Console.WriteLine(string.Join(", ", numbers));

        QuickSort(numbers, 0, numbers.Length - 1);

        Console.WriteLine("\nОтсортированный массив:");
        Console.WriteLine(string.Join(", ", numbers));
        
        Console.ReadKey();
    }

    static void QuickSort(int[] array, int left, int right)
    {
        if (left < right)
        {
            int pivotIndex = Partition(array, left, right);

            QuickSort(array, left, pivotIndex - 1);
            QuickSort(array, pivotIndex + 1, right);
        }
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
                Swap(array, i, j);
            }
        }

        Swap(array, i + 1, right);
        return i + 1;
    }

    static void Swap(int[] array, int a, int b)
    {
        int temp = array[a];
        array[a] = array[b];
        array[b] = temp;
    }
}

