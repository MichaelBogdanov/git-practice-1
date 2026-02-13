def bubble_sort(arr):
    n = len(arr)
    # проходим по всем элементам массива
    for i in range(n):
        # последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            # меняем элементы, если текущий больше следующего
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    user_input = input("Введите числа через пробел: ")
    try:
        data = [float(x) for x in user_input.split()]
        sorted_data = bubble_sort(data)
        print(f"Отсортированный список: {sorted_data}")
    except ValueError:
        print("Ошибка: введите корректные числа.")