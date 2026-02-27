# Задача 06 — Сортировка слиянием (Merge Sort)
# Без использования встроенных функций сортировки (sort, sorted и т.д.)
# Сложность: O(n log n) по времени, O(n) по памяти


def merge_sort(arr):
    """
    Сортировка слиянием.
    Идея: делим список пополам рекурсивно, пока не останутся
    списки из 1 элемента, затем сливаем их обратно по порядку.
    """
    # База рекурсии: список из 0 или 1 элемента уже отсортирован
    if len(arr) <= 1:
        return arr

    # Делим список на две половины
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # рекурсивно сортируем левую
    right = merge_sort(arr[mid:])  # рекурсивно сортируем правую

    # Сливаем два отсортированных списка в один
    return merge(left, right)


def merge(left, right):
    """Сливает два отсортированных списка в один отсортированный."""
    result = []
    i = 0  # указатель для left
    j = 0  # указатель для right

    # Сравниваем элементы обоих списков и добавляем меньший
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы (один из списков уже закончился)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# --- Запуск ---
if __name__ == "__main__":
    print("Сортировка слиянием")
    print("Введите числа через пробел:")

    user_input = input("> ").strip()
    try:
        numbers = [int(x) for x in user_input.split()]
        sorted_numbers = merge_sort(numbers)
        print(f"Результат: {sorted_numbers}")
    except ValueError:
        print("Ошибка: введите целые числа через пробел")
