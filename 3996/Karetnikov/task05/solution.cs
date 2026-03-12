using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите число:");
        string input = Console.ReadLine();
        
        if (input[0] >= '0' && input[0] <= '9')
        {
            int num = int.Parse(input);
            string result = "";
            
            string[] m = { "", "M", "MM", "MMM" };
            string[] c = { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" };
            string[] x = { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" };
            string[] i = { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" };
            
            result = m[num / 1000] + c[(num % 1000) / 100] + x[(num % 100) / 10] + i[num % 10];
            Console.WriteLine(result);
        }
        else
        {
            int result = 0;
            for (int j = 0; j < input.Length; j++)
            {
                if (input[j] == 'I') result += 1;
                if (input[j] == 'V') result += 5;
                if (input[j] == 'X') result += 10;
                if (input[j] == 'L') result += 50;
                if (input[j] == 'C') result += 100;
                if (input[j] == 'D') result += 500;
                if (input[j] == 'M') result += 1000;
            }
            
            if (input.Contains("IV") || input.Contains("IX")) result -= 2;
            if (input.Contains("XL") || input.Contains("XC")) result -= 20;
            if (input.Contains("CD") || input.Contains("CM")) result -= 200;
            
            Console.WriteLine(result);
        }
    }
}