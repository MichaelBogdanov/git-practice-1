using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace task8
{
    public class PasswordGenerator
    {
        private static readonly Random random = new Random();

        private const string Digits = "0123456789";
        private const string Lowercase = "abcdefghijklmnopqrstuvwxyz";
        private const string Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        private const string SpecialChars = "!@#$%^&*()_-+=<>?";

        public static string Generate(int length,
                                      bool includeDigits = true,
                                      bool includeLowercase = true,
                                      bool includeUppercase = true,
                                      bool includeSpecial = true)
        {
            if (length <= 0)
                throw new ArgumentException("Длина должна быть больше 0");

            // собираем доступные наборы символов
            var charSets = new List<string>();
            if (includeDigits) charSets.Add(Digits);
            if (includeLowercase) charSets.Add(Lowercase);
            if (includeUppercase) charSets.Add(Uppercase);
            if (includeSpecial) charSets.Add(SpecialChars);

            if (charSets.Count == 0)
                throw new ArgumentException("Должен быть выбран хотя бы один набор символов");

            // проверяем минимальную длину
            if (length < charSets.Count)
                throw new ArgumentException($"Длина должна быть не меньше {charSets.Count} для выбранных наборов");

            var result = new StringBuilder(length);

            // гарантируем по одному символу из каждого выбранного набора
            foreach (var set in charSets)
            {
                result.Append(set[random.Next(set.Length)]);
            }

            // заполняем оставшуюся длину случайными символами из всех наборов
            string allChars = string.Join("", charSets);
            for (int i = charSets.Count; i < length; i++)
            {
                result.Append(allChars[random.Next(allChars.Length)]);
            }

            // перемешиваем результат
            return Shuffle(result.ToString());
        }

        private static string Shuffle(string input)
        {
            char[] chars = input.ToCharArray();
            for (int i = chars.Length - 1; i > 0; i--)
            {
                int j = random.Next(i + 1);
                (chars[i], chars[j]) = (chars[j], chars[i]);
            }
            return new string(chars);
        }
    }

    // пример использования
    class Program
    {
        static void Main()
        {
            // пароль длиной 12 со всеми типами символов
            string password1 = PasswordGenerator.Generate(12);
            Console.WriteLine($"Пароль 1: {password1}");

            // только цифры и строчные буквы
            string password2 = PasswordGenerator.Generate(8,
                includeDigits: true,
                includeLowercase: true,
                includeUppercase: false,
                includeSpecial: false);
            Console.WriteLine($"Пароль 2: {password2}");

            // только прописные и спецсимволы
            string password3 = PasswordGenerator.Generate(10,
                includeDigits: false,
                includeLowercase: false,
                includeUppercase: true,
                includeSpecial: true);
            Console.WriteLine($"Пароль 3: {password3}");
        }
    }
}
