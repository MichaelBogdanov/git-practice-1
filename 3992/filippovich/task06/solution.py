import sys

def quicksort(arr):
    "Быстрая сортировка: деление на три части относительно опорного элемента"
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    if len(sys.argv) != 2:
        print("Использование: python solution.py <файл с числами>")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            data = f.read().strip().split()
            numbers = [int(x) for x in data]
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        sys.exit(1)
    sorted_numbers = quicksort(numbers)
    print("Отсортированный массив:", ' '.join(map(str, sorted_numbers)))

if __name__ == "__main__":
    main()