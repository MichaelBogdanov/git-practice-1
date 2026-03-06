using System.Text.RegularExpressions;

namespace _3Задание
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
          
                string inputFilePath = "input.txt";
                string outputFilePath = "output.txt";

          
                if (!File.Exists(inputFilePath))
                {
                    File.WriteAllText(inputFilePath, "Привет! Как дела?");
                }

                string content = File.ReadAllText(inputFilePath);

                
                string[] words = Regex.Split(content.Trim(), " ");


                Array.Reverse(words);

                
                string result = string.Join(" ", words);

              
                File.WriteAllText(outputFilePath, result);

                Console.WriteLine("Операция выполнена успешно!");
                Console.WriteLine($"Результат сохранен в файл: {outputFilePath}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка: {ex.Message}");
            }
        }
    }
}
