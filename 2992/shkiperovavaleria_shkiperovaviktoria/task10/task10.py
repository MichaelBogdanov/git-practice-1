import string

# допустимые шестнадцатеричные символы (0-9, a-f, A-F)
HEX_DIGITS = set(string.hexdigits)
def is_ipv4(ip: str) -> bool:
    # разделение строки по точкам на 4 части
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit():
            return False
        # проверка диапазона от 0 до 255
        if not 0 <= int(p) <= 255:
            return False
        # проверка на лидирующие нули (например, "01"), кроме "0"
        if p != "0" and p[0] == "0":
            return False
    return True

def is_ipv6(ip: str):
    # проверка не более одного "::"
    if ip.count("::") > 1:
        return False, None

    if "::" in ip:
        # разбиение адреса на частьи слева и справа от "::"
        left, right = ip.split("::")
        left_parts = left.split(":") if left else []
        right_parts = right.split(":") if right else []
        # проверка что частей не больше 8
        if len(left_parts) + len(right_parts) > 8:
            return False, None
        # подсчет сколько "нулевых" блоков нужно вставить вместо "::"
        missing = 8 - (len(left_parts) + len(right_parts))
        parts = left_parts + (["0"] * missing) + right_parts
    else:
        parts = ip.split(":")
        if len(parts) != 8:
            return False, None

    normalized_parts = []
    for p in parts:
        if len(p) == 0 or len(p) > 4:
            return False, None
        # все символы блока должны быть шестнадцатеричными
        if not all(ch in HEX_DIGITS for ch in p):
            return False, None
        # удаление лишних нулей и превращение блока в число в 16‑й системе
        normalized_parts.append(str(int(p, 16)))

    # нормализованный IPv6 (все блоки без ведущих нулей)
    norm = ":".join(format(int(x), "x") for x in normalized_parts)
    return True, norm

def main():
    s = input().strip()
    if is_ipv4(s):
        print("IPv4")
        return

    ok6, norm6 = is_ipv6(s)
    if ok6:
        print("IPv6")
        print(norm6)
        return
    print("INVALID")


if __name__ == "__main__":
    main()
