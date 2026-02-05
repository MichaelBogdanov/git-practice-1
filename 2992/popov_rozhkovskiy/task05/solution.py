#конвертация в римские числа
def to_roman(n):
    if n < 1 or n > 3999:
        return "ошибка"
    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    for v, s in zip(vals, syms):
        while n >= v:
            res += s
            n -= v
    return res

#конвертация в арабските числа
def to_arabic(s):
    s = s.strip().upper()
    if not s or any(c not in "IVXLCDM" for c in s):
        return "ошибка"
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for c in reversed(s):
        val = d[c]
        total = total - val if val < prev else total + val
        prev = val
   #проверка
    if to_roman(total) != s:
        return "ошибка"
    return total


# основная часть
inp = input("Введите число (арабское или римское): ").strip()

if inp.isdigit():
    num = int(inp)
    print(to_roman(num))
else:
    print(to_arabic(inp))
