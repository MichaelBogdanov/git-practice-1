using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Сколько символов?");
        int len = int.Parse(Console.ReadLine());
        
        string symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";
        string password = "";
        
        Random rnd = new Random();
        
        for (int i = 0; i < len; i++)
        {
            int index = rnd.Next(symbols.Length);
            password = password + symbols[index];
        }
        
        Console.WriteLine("Пароль: " + password);
    }
}