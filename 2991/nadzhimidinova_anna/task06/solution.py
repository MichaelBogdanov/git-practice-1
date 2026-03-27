def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers[:]

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return merge(left, right)


def parse_input(text):
    parts = text.strip().split()
    numbers = []

    for part in parts:
        numbers.append(int(part))

    return numbers


def main():
    user_input = input("Введите числа через пробел: ")
    numbers = parse_input(user_input)
    sorted_numbers = merge_sort(numbers)
    print("Отсортированный список:", *sorted_numbers)


if __name__ == "__main__":
    main()