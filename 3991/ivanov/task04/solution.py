# Очистка файла от дубликатов, сохраняя порядок
def clear_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.read()

    words_set = set()
    words_order = list()

    current_word = ""

    for ch in lines:
        # Если символ является пробельным,
        # обрабатываем последнее слово
        if ch in [" ", "\n", "\t"]:
            # Пропускаем пустые слова
            if not current_word:
                continue

            # Если слово уже было встречено,
            # пропускаем его
            if current_word in words_set:
                current_word = ""
                continue

            # Добавляем слово в множество и список
            words_set.add(current_word)
            words_order.append(current_word)
            current_word = ""

        # Если символ не является пробельным,
        # добавляем его к текущему слову
        else:
            current_word += ch

    # Обрабатываем последнее слово
    if current_word:
        if current_word not in words_set:
            words_set.add(current_word)
            words_order.append(current_word)
    
    # Возвращаем результат в виде строки
    return " ".join(words_order)
