using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace task6
{
    public class BubbleSort
    {
        public static void Sort(int[] array)
        {
            int n = array.Length;
            for (int i = 0; i < n - 1; i++)
            {
                for (int j = 0; j < n - i - 1; j++)
                {
                    if (array[j] > array[j + 1])
                    {
                        int temp = array[j];
                        array[j] = array[j + 1];
                        array[j + 1] = temp;
                    }
                }
            }
        }
    }

    class Program
    {
        static void Main()
        {
            int[] numbers = { 64, 34, 25, 12, 22, 11, 90 };

            Console.WriteLine("Исходный массив: " + string.Join(", ", numbers));

            BubbleSort.Sort(numbers);

            Console.WriteLine("Отсортированный массив: " + string.Join(", ", numbers));
        }
    }
}
