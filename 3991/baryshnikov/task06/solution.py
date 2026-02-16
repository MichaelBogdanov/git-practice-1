def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


array = [0, -12, 45, 11, 120, -65, 12, 65, 4, 9]
print(bubble_sort(array))