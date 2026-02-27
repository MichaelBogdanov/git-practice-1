import sys
import os

def main():
    # проверка указан ли файл
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Ошибка: указаны неправильные аргументы")
        print("Примеры как можно: python solution.py input.txt или python solution.py input.txt --ignore-case")
        return
    
    filename = sys.argv[1]
    
    # проверка существует ли файл
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не найден")
        return
    
    # проверка опции игнорирования регистра
    ignore_case = len(sys.argv) == 3 and sys.argv[2] == "--ignore-case"
    
    try:
        # читает файл
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # если нужно проигнорировать регистр
        if ignore_case:
            text = text.lower()
        
        # считаем частоту 
        freq = {}
        for c in text:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        # Сортировка по убыванию
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        print("Частота символов:")
        for char, count in sorted_freq:
            print(f"'{char}': {count}")
            
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

if __name__ == "__main__":
    main()