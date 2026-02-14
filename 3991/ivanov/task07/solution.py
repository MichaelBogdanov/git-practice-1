# Вычисление частоты символов в файле
def count_frequency(filename, ignore_case=False, sort_output=False):
    with open(filename, 'r') as file:
        text = file.read()

    # Словарь частоты каждого символа
    freqs = dict()

    for ch in text:
        # Если включена опция игнорирования регистра
        # то преобразуем все символы в нижний регистр
        if ignore_case:
            ch = ch.lower()
    
        if ch in freqs:
            freqs[ch] += 1
        else:
            freqs[ch] = 1

    if not sort_output:
        return freqs

    # Сортировка по частоте
    sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    return sorted_freqs