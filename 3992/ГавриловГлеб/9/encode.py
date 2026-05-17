try:
    s = input().strip()
    r = []
    c = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            c += 1
        else:
            r.append(s[i-1] + str(c))
            c = 1
    if s:
        r.append(s[-1] + str(c))
    print("".join(r))
except Exception:
    print("Ошибочка")
