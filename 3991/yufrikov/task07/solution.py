def counterSymbols(text, registr=False):
    if registr:
        text = text.lower() # проверка на регистр
    freq = {}

    for i in text:
        if i != ' ':
            if i in freq:
                freq[i] += 1 # прибавление к сущетсвущему символу
            else :
                freq[i] = 1 # добавлние в словрь
    
    items = list(freq.items())
    
    n = len(items)
    for i in range(n): # сортировка пузырьком
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:  
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return dict(items)


# print(counterSymbols("ghфjb sjgfkn dsafjn"))