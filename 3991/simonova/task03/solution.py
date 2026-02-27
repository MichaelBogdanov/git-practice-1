import sys
import os

def main():
    # проверка указан ли файл
    if len(sys.argv) != 2:
        print("Ошибка: не указан входной файл")
        print("Пример как надо: python solution.py input.txt")
        return
    
    filename = sys.argv[1]
    
    # проверка существует ли файл
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не найден")
        return
    
    try:
        # читает файл
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # разбиваем на слова, переворачиваем и соединяем
        words = text.split()
        words.reverse()
        result = ' '.join(words)
        
        print(result)
        
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

if __name__ == "__main__":
    main()