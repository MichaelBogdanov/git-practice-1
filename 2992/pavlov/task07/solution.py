import sys

def count_characters(filename, ignore_case=False):
    """Подсчитывает частоту символов в файле"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            
        # Создаем словарь для подсчета
        freq = {}
        for char in text:
            if ignore_case:
                char = char.lower()
            
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        # Сортируем по убыванию частоты
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_freq, len(text)
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
        return [], 0
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return [], 0

def main():
    if len(sys.argv) < 2:
        print("Пример: python script.py text.txt")
         # Пример с игнорированием регистра
        print("Пример: python script.py text.txt --ignore-case")
        return
    
    filename = sys.argv[1]
    ignore_case = "--ignore-case" in sys.argv
    
    print(f"Анализ файла: {filename}")
    print(f"Игнорировать регистр: {'Да' if ignore_case else 'Нет'}")
    print("-" * 40)
    
    freq, total_chars = count_characters(filename, ignore_case)
    
    if not freq:
        return
    
    print(f"Всего символов в файле: {total_chars}")
    print(f"Уникальных символов: {len(freq)}")
    print()
    print("Частота символов (по убыванию):")
    print("-" * 40)
    print("Символ | Частота | Процент")
    print("-" * 40)
    for char, count in freq:
        # Для отображения специальных символов
        display_char = repr(char)[1:-1] if char in '\n\t\r' else char
        
        percentage = (count / total_chars) * 100
        print(f"{display_char:^6} | {count:^7} | {percentage:^7.2f}%")

if __name__ == "__main__":
    main()