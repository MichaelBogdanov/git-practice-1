using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите IP:");
        string ip = Console.ReadLine();

        string[] nums = ip.Split('.');

        if (nums.Length != 4)
        {
            Console.WriteLine("Неверный IP");
            return;
        }

        for (int i = 0; i < 4; i++)
        {
            if (nums[i] == "")
            {
                Console.WriteLine("Неверный IP");
                return;
            }

            if (nums[i].Length > 1 && nums[i][0] == '0')
            {
                Console.WriteLine("Неверный IP");
                return;
            }

            int num = 0;
            try
            {
                num = int.Parse(nums[i]);
            }
            catch
            {
                Console.WriteLine("Неверный IP");
                return;
            }

            if (num < 0 || num > 255)
            {
                Console.WriteLine("Неверный IP");
                return;
            }
        }

        Console.WriteLine("Верный IP");
    }
}