using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Program {
    static void Main() {
        string fileName = "input.txt"; 

        if (!File.Exists(fileName)) {
            Console.WriteLine($"Ошибка: Файл {fileName} не найден в папке с программой.");
            return;
        }

        try {
            string text = File.ReadAllText(fileName).ToLower();
            var charCounts = new Dictionary<char, int>();

            foreach (char c in text) {
                if (char.IsControl(c)) continue;

                if (charCounts.ContainsKey(c)) {
                    charCounts[c]++;
                } else {
                    charCounts[c] = 1;
                }
            }

            var sortedChars = charCounts.OrderByDescending(x => x.Value);

            Console.WriteLine($"Статистика для файла {fileName}:");
            foreach (var pair in sortedChars) {
                Console.WriteLine($"'{pair.Key}': {pair.Value}");
            }
        }
        catch (Exception ex) {
            Console.WriteLine($"Ошибка при обработке файла: {ex.Message}");
        }
    }
}
