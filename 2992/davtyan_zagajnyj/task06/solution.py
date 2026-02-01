def quick_sort(arr):
    """
    Реализация алгоритма быстрой сортировки (Quick Sort)
    """
    # Базовый случай: если массив пустой или состоит из одного элемента, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент — в данном случае средний элемент
    pivot = arr[len(arr) // 2]

    # Распределяем элементы по трем спискам
    left = [x for x in arr if x < pivot]    # Меньше опорного
    middle = [x for x in arr if x == pivot] # Равные опорному
    right = [x for x in arr if x > pivot]   # Больше опорного

    # Рекурсивно сортируем левую и правую части и объединяем результат
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    test_list = [38, 27, 43, 3, 9, 82, 10, 10, 5]
    print(f"Исходный список: {test_list}")

    sorted_list = quick_sort(test_list)
    print(f"Отсортированный список: {sorted_list}")