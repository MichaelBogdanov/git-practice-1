try:
    s = input().strip()
    r = []
    i = 0
    while i < len(s):
        ch = s[i]
        i += 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        r.append(ch * int(num))
    print("".join(r))
except Exception:
    print("Ошибка")
