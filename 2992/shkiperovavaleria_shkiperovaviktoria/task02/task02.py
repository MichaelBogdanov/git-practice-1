import string
import os

def analyze_file(filename):
    lines_count = 0
    words_count = 0
    longest = ""
    
    punct = set(string.punctuation)
    
    # проверка существования файла
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не найден!")
        return 0, 0, "", 0
    
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines_count += 1
            # замена пунктуации на пробел
            cleaned = "".join(ch if ch not in punct else " " for ch in line)
            words = cleaned.split()
            words_count += len(words)
            for w in words:
                if len(w) > len(longest):
                    longest = w
    return lines_count, words_count, longest, len(longest)

if __name__ == "__main__":
    filename = "text.txt"
    lines, words, longest, longest_len = analyze_file(filename)
    print("Строк:", lines)
    print("Слов:", words)
    print("Самое длинное слово:", longest)
    print("Длина слова:", longest_len)
