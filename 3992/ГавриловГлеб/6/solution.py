inp = list(map(int, input().split()))
for i in range(len(inp)-1):
    for j in range(len(inp)-i-1):
        if inp[j] > inp[j + 1]:
            inp[j], inp[j + 1] = inp[j + 1], inp[j]

print(*inp)
