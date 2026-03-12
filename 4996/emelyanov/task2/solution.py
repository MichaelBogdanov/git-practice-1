import sys
import string

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        all_words = []
        for line in lines:
            # Очищаем строку от пунктуации и разбиваем на слова
            clean_line = line.translate(str.maketrans('', '', string.punctuation))
            all_words.extend(clean_line.split())

        line_count = len(lines)
        word_count = len(all_words)
        
        if all_words:
            longest_word = max(all_words, key=len)
            return line_count, word_count, longest_word, len(longest_word)
        return line_count, 0, "Нет слов", 0

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)

if __name__ == "__main__":
    # Проверяем, передан ли аргумент (имя файла)
    if len(sys.argv) < 2:
        print("Использование: python solution.py <имя_файла.txt>")
        sys.exit(1)

    filename = sys.argv[1]
    l_count, w_count, max_w, max_l = analyze_file(filename)

    print(f"--- Результаты анализа файла: {filename} ---")
    print(f"Строк: {l_count}")
    print(f"Слов: {w_count}")
    print(f"Самое длинное слово: '{max_w}' ({max_l} симв.)")