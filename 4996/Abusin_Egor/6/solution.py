# Задача 6: Сортировка (без встроенных функций)
# Реализация быстрой сортировки (Quick Sort)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr

print("=" * 50)
print("Задача 6: Сортировка (без встроенных функций)")
print("=" * 50)

# Тестовые данные
test_arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 8, 1, 9, 3],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1]
]

for arr in test_arrays:
    print(f"\nИсходный: {arr}")
    
    sorted_quick = quick_sort(arr.copy())
    print(f"QuickSort: {sorted_quick}")
    
    sorted_bubble = bubble_sort(arr.copy())
    print(f"BubbleSort: {sorted_bubble}")

# Интерактивный режим
print("\n" + "=" * 50)
print("Интерактивный режим")
print("Введите числа через пробел:")

user_input = input("> ").strip()
if user_input:
    numbers = [int(x) for x in user_input.split()]
    print(f"Исходный: {numbers}")
    print(f"Отсортированный: {quick_sort(numbers)}")