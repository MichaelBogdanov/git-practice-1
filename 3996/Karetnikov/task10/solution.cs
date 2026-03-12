using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите IP:");
        string ip = Console.ReadLine();
        
        string[] parts = ip.Split('.');
        
        if (parts.Length != 4)
        {
            Console.WriteLine("Неверный IP");
            return;
        }
        
        for (int i = 0; i < 4; i++)
        {
            if (parts[i] == "")
            {
                Console.WriteLine("Неверный IP");
                return;
            }
            
            int num = 0;
            try
            {
                num = int.Parse(parts[i]);
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
            
            if (parts[i].Length > 1 && parts[i][0] == '0')
            {
                Console.WriteLine("Неверный IP");
                return;
            }
        }
        
        Console.WriteLine("Верный IP");
    }
}