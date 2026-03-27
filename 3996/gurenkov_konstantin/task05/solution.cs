using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Zadacha5
{
    internal class Program
    {
        static Dictionary<char, int> map = new Dictionary<char, int>()
    {
        {'I',1}, {'V',5}, {'X',10},
        {'L',50}, {'C',100},
        {'D',500}, {'M',1000}
    };
        static string ToRoman(int num)
        {
            string[] thousands = { "", "M", "MM", "MMM" };
            string[] hundreds = { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" };
            string[] tens = { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" };
            string[] ones = { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" };

            return thousands[num / 1000] + hundreds[(num % 1000) / 100] + tens[(num % 100) / 10] + ones[num % 10];
        }
        static bool IsValid(string s)
        {
            foreach (char c in s)
                if (!map.ContainsKey(c))
                    return false;

            return true;
        }
        static int ToArabic(string s)
        {
            if (!IsValid(s))
                throw new Exception("Ошибка: неверные символы");
            int sum = 0;
            for (int i = 0; i < s.Length; i++)
            {
                int current = map[s[i]];

                if (i + 1 < s.Length && current < map[s[i + 1]])
                    sum -= current;
                else
                    sum += current;
            }
            return sum;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(ToRoman(58));      
            Console.WriteLine(ToArabic("MCM"));   
        }
    }
}
