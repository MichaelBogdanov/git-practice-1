class Program
{
    static void Main(string[] args)
    {
        int[] array = { 12, 100, 25, 313, 42, 52, 67, 69, };
        Console.WriteLine("До сортировки");
        PrintArray(array);
        BubbleSort(array);
        Console.WriteLine("После сортировки");
        PrintArray(array);
    }

    // Функция сортировки пузырьком
    static void BubbleSort(int[] array)
    {
        int size = array.Length;
        bool swapped;
        for (int i = 0; i < size - 1; i++)
        {
            swapped = false;
            for (int j = 0; j < size - 1; j++)
            {
                if (array[j] > array[j + 1])
                {
                    swapped = true;
                    int temp;
                    temp = array[i];
                    array[i] = array[j + 1];
                    array[j] = temp;
                }
            }
            if (!swapped)
            {
                break;
            }
        }
    }
    static void PrintArray(int[] array)
    {
        foreach (int item in array)
        {
            Console.Write(item + " ");
        }
        Console.WriteLine();
    }
}