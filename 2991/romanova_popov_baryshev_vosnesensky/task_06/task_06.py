arr = list(map(int, input().split()))

def func(a):
    swapped = False
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            swapped = True
    if swapped:
        return func(a)
    return a

print(func(arr))