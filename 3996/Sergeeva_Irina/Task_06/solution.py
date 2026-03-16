def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    
    # Внешний цикл - количество проходов
    for i in range(n-1):
        # Внутренний цикл - сравнение соседних элементов
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                # Обмен элементов
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
