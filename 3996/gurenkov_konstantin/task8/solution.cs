using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Zadacha8
{
    internal class Program
    {
        static Random rnd = new Random();

        static string GeneratePassword(int length, bool useDigits, bool useLower, bool useUpper, bool useSpecial)
        {
            string digits = "0123456789";
            string lower = "abcdefghijklmnopqrstuvwxyz";
            string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            string special = "!@#$%^&*";
            List<string> selectedSets = new List<string>();
            if (useDigits) selectedSets.Add(digits);
            if (useLower) selectedSets.Add(lower);
            if (useUpper) selectedSets.Add(upper);
            if (useSpecial) selectedSets.Add(special);
            if (selectedSets.Count == 0)
                throw new Exception("Нужно выбрать хотя бы один набор символов");
            if (length < selectedSets.Count)
                throw new Exception("Длина пароля слишком мала для всех выбранных наборов");
            List<char> password = new List<char>();
            foreach (var set in selectedSets)
            {
                password.Add(set[rnd.Next(set.Length)]);
            }
            string allChars = string.Join("", selectedSets);
            while (password.Count < length)
            {
                password.Add(allChars[rnd.Next(allChars.Length)]);
            }
            for (int i = 0; i < password.Count; i++)
            {
                int j = rnd.Next(password.Count);
                (password[i], password[j]) = (password[j], password[i]);
            }
            return new string(password.ToArray());
        }

        static void Main(string[] args)
        {
            string password = GeneratePassword(length: 10,useDigits: true,useLower: true,useUpper: true,useSpecial: true);

            Console.WriteLine(password);
        }
    }
}

