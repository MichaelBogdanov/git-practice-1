str = input()
res = ""

for i in str:
    if i not in res:
        res += i
print(res)