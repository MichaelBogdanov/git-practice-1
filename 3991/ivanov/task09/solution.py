# Сжатие файла
def compress_RLE(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()

    result = ""

    prev_ch = "" # Предыдущий символ
    ch_count = 0 # Подсчёт одинаковых символов

    for ch in text:
        # Подсчитываем, сколько одинаковых символов идут подряд
        if ch == prev_ch:
            ch_count += 1
        else:
            # Если символ изменился, записываем предыдущий символ и его количество
            if prev_ch:
                # Экранируем цифры и спецсимволы
                if prev_ch in "0123456789\\":
                    result += f"\\{prev_ch}{ch_count}"
                else:
                    result += f"{prev_ch}{ch_count}"

            ch_count = 1
            prev_ch = ch

    # Записываем последний символ
    if prev_ch:
        # Экранируем цифры и спецсимволы
        if prev_ch in "0123456789\\":
            result += f"\\{prev_ch}{ch_count}"
        else:
            result += f"{prev_ch}{ch_count}"

    # Сохраняем результат в файл
    with open(output_file, 'w') as f:
        f.write(result)


# Распаковка файла
def decompress_RLE(input_file, output_file):
    with open(input_file, 'r') as f:
        compressed_text = f.read()

    result = ""
    i = 0
    
    while i < len(compressed_text):
        # Проверяем, является ли текущий символ экранирующим
        if compressed_text[i] == '\\':
            # Пропускаем обратную косую черту
            i += 1
            # Следующий символ - это символ, который был заэкранирован
            char = compressed_text[i]
            i += 1
            # Считываем число повторений
            count = ""
            while i < len(compressed_text) and compressed_text[i].isdigit():
                count += compressed_text[i]
                i += 1
            # Добавляем символ нужное количество раз
            result += char * int(count)
        else:
            # Обычный символ (не экранированный)
            char = compressed_text[i]
            i += 1
            # Считываем число повторений
            count = ""
            while i < len(compressed_text) and compressed_text[i].isdigit():
                count += compressed_text[i]
                i += 1
            # Добавляем символ нужное количество раз
            result += char * int(count)
    
    # Сохраняем результат в файл
    with open(output_file, 'w') as f:
        f.write(result)