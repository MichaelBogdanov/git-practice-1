using System;
using System.Linq;

class Program
{
    static bool IsValidIP(string ip)
    {
        string[] parts = ip.Split('.');
        
        if (parts.Length != 4)
            return false;
        
        foreach (string part in parts)
        {
            if (string.IsNullOrEmpty(part))
                return false;
            
            if (part.Length > 1 && part[0] == '0')
                return false;
            
            if (!part.All(char.IsDigit))
                return false;
            
            int num = int.Parse(part);
            if (num < 0 || num > 255)
                return false;
        }
        
        return true;
    }

    static void Main()
    {
        Console.Write("Введите IP-адрес: ");
        string ip = Console.ReadLine();
        
        if (IsValidIP(ip))
            Console.WriteLine("Корректный IP-адрес");
        else
            Console.WriteLine("Некорректный IP-адрес");
    }
}