def merge_sort(arr: list) -> list:
    """Сортировка набора чисел слиянием"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    
    return result

def read_from_file(file: str):
    """Читать набор чисел из файла"""
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
            numbers = []
            for arr in data.split():
                try:
                    numbers.append(float(arr))
                except ValueError:
                    continue
            return numbers
        
    except Exception as e:
       return []

if __name__ == "__main__":
    from random import randint
    import sys
    
    arr = []
    if len(sys.argv) == 1:
        arr = [randint(1, 100) for _ in range(50)]
    elif len(sys.argv) == 2:
        file = sys.argv[1]
        arr = read_from_file(file)
        if not arr:
            print("python solution.py file.txt")
            print('Ошибка: Не удалось прочитать числа из файла')
            sys.exit(1)
    else:
        try:
            arr = [int(x) for x in sys.argv[1:]]
        except ValueError:
            print("python solution.py 1 5 4 3")
            print("Ошибка: Все аргументы должны быть числами")
            sys.exit(1)
    
    sorted_arr = merge_sort(arr)
    print("Результат:", " ".join(map(str, sorted_arr)))
