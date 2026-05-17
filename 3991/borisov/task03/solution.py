import sys
import os

def reverse_words():
    # Проверяем, передан ли путь к файлу в аргументах
    if len(sys.argv) < 2:
        print("Использование: python solution.py <путь_к_файлу>")
        return

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Ошибка: Файл {file_path} не найден.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        words = content.split()
        reversed_content = " ".join(words[::-1])

        # Результат
        print(reversed_content)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    reverse_words()