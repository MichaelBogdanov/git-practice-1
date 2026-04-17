import string

def count_stats(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
        return None
    
    # Разбиваем на строки
    lines = text.splitlines()
    num_lines = len(lines)
    
    # Убираем знаки пунктуации и разбиваем на слова
    translator = str.maketrans('', '', string.punctuation)
    words = []
    for line in lines:
        # Убираем пунктуацию и разбиваем по пробелам
        clean_line = line.translate(translator)
        for word in clean_line.split():
            if word:  # игнорируем пустые строки
                words.append(word)
    
    num_words = len(words)
    
    # Находим самое длинное слово
    if words:
        longest_word = max(words, key=len)
        longest_length = len(longest_word)
    else:
        longest_word = "нет слов"
        longest_length = 0
    
    return num_lines, num_words, longest_word, longest_length

# Запуск
filename = input("Введите имя файла: ")
result = count_stats(filename)

if result:
    lines, words, longest, length = result
    print(f"\n--- Результаты ---")
    print(f"Количество строк: {lines}")
    print(f"Количество слов: {words}")
    print(f"Самое длинное слово: '{longest}' (длина: {length})")