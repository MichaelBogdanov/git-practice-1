import re
import string

def analyze_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Подсчет строк (по \n)
        lines = len(content.splitlines())
        
        # Очистка от пунктуации и разделение на слова
        translator = str.maketrans('', '', string.punctuation)
        clean_text = content.translate(translator)
        words = clean_text.split() 
        
        word_count = len(words)
        
        # Находим самое длинное слово
        if words:
            longest_word = max(words, key=len)
            longest_length = len(longest_word)
        else:
            longest_word = ""
            longest_length = 0
        
        return {
            'строк': lines,
            'слов': word_count,
            'самое длинное слово': longest_word,
            'его длина': longest_length
        }
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Выполнение анализа
result = analyze_text_file('input.txt')

if result:
    print(f"Количество строк: {result['строк']}")
    print(f"Количество слов: {result['слов']}")
    print(f"Самое длинное слово: '{result['самое длинное слово']}'")
    print(f"Длина самого длинного слова: {result['его длина']}")
