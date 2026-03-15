using System.Collections.Specialized;
using System.ComponentModel.Design;
using System.Runtime.InteropServices;
using System.Text;

namespace random_password
{
    class Program
    {
        static bool isNumbers = true;
        static bool isUpper = true;
        static bool isSpecial = true;
        static void Main(string[] args)
        {
            Menu();
        }
        //Метод генерации пароля
        static public void GeneratePassword()
        {
            Console.WriteLine("Введите длину пароля");
            int length = Convert.ToInt32(Console.ReadLine());

            string lowerChars = "abcdefghijklmnopqrstuvwxyz";
            string upperChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            string numbers = "0123456789";
            string specials = "!@#$%^&*()_+-=[]{}|;:,.<>?/`~\\\"'";

            int countOptions = 1;
            if (isNumbers) countOptions++;
            if(isSpecial) countOptions++;
            if(isUpper) countOptions++;
            var result = new List<char>(length);

            if(length <= 0)
            {
                Console.WriteLine("Не верная длина пароля");
                return;
            }
            if (countOptions > length)
            {
                AddCharToList(result, lowerChars, length);
                result = result.OrderBy(x => Random.Shared.Next()).ToList();
                string password = new string(result.ToArray());
                Console.WriteLine($"Пароль: {password}");
                return;
            }
            else
            {
                AddCharToList(result, lowerChars, length/countOptions);
                if (isNumbers)
                {
                    AddCharToList(result, numbers, length/countOptions);
                }
                if (isUpper)
                {
                    AddCharToList(result, upperChars, length / countOptions);
                }
                if (isSpecial)
                {
                    AddCharToList(result, specials, length / countOptions);
                }

                result = result.OrderBy(x => Random.Shared.Next()).ToList();
                string pass = new string(result.ToArray());
                Console.WriteLine($"Пароль: {pass}");
                return;
            }

        }

        //Метод выбора опций
        static public void Menu()
        {
            Console.WriteLine("Генератор пароля");
            Console.WriteLine("Выберите пункт меню:");
            Console.WriteLine("1. Выключить/Включить цифры в пароле");
            Console.WriteLine("2. Включить/Включить прописные буквы");
            Console.WriteLine("3. Включить/Выключить специальные символы");
            Console.WriteLine("4. Сгенерировать пароль");
            int answer = Convert.ToInt32(Console.ReadLine());

            do
            {
                switch (answer)
                {
                    case 1:
                        isNumbers = !isNumbers;
                        if (isNumbers)
                        {
                            Console.WriteLine("Цифры в пароле включены");
                        }
                        else
                        {
                            Console.WriteLine("Цифры в пароле выключены");
                        }
                        Menu();
                        break;
                    case 2:
                        isUpper = !isUpper;
                        if (isUpper)
                        {
                            Console.WriteLine("Заглавные буквы в пароле включены");
                        }
                        else
                        {
                            Console.WriteLine("Заглавные буквы в пароле выключены");
                        }
                        Menu();
                        break;
                    case 3:
                        isSpecial = !isSpecial;
                        if (isSpecial)
                        {
                            Console.WriteLine("Специальные символы в пароле включены");
                        }
                        else
                        {
                            Console.WriteLine("Специальные символы в пароле выключены");
                        }
                        Menu();
                        break;
                    case 4:
                        Console.WriteLine();
                        GeneratePassword();
                        break;
                    default:
                        Console.WriteLine("Не верный вариант ответа");
                        Menu();
                        break;
                }
            } while (answer != 4);
        }
        //Метод добавление символов в список
        static void AddCharToList(List<char> list, string currentString, int length)
        {
            for (int i = 0; i < length; i++)
            {
                list.Add(currentString[Random.Shared.Next(currentString.Length)]);
            }
        }
    }
}