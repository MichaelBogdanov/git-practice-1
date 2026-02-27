import sys
import os

def main():
    # проверка указан ли файл
    if len(sys.argv) != 2:
        print("Ошибка: не указан входной файл")
        print("пример как надо: python solution.py input.txt")
        return
    
    filename = sys.argv[1]
    
    # проверка существует ли файл
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не найден")
        return
    
    try:
        # читает файл
        with open(filename, 'r', encoding='utf-8') as f:
            elements = f.read().split()
        
        # удаляем дубликаты
        seen = set()
        result = []
        
        for item in elements:
            if item not in seen:
                seen.add(item)
                result.append(item)
        
        print(' '.join(result))
        
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

if __name__ == "__main__":
    main()