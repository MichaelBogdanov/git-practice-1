listNumbers = [0, 2, 4, 3, 1]

n = len(listNumbers)
middle = 0
for i in range(n):
    for j in range(n):
        if listNumbers[i] > listNumbers[j]:
            middle = listNumbers[i]
            listNumbers[i] = listNumbers[j]
            listNumbers[j] = middle

print(listNumbers)
