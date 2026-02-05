def check_ip(s):
    s = s.strip()

    #проверка на IPv4
    if '.' in s and ':' not in s:
        parts = s.split('.')
        if len(parts) != 4:
            return "INVALID"
        for p in parts:
            if not p.isdigit() or not (0 <= int(p) <= 255):
                return "INVALID"
            if len(p) > 1 and p[0] == '0':  
                return "INVALID"
        return "IPv4"

    #проверка на IPv6
    if ':' in s and '.' not in s:
        parts = s.split(':')
        if not (2 <= len(parts) <= 8):
            return "INVALID"
        for p in parts:
            if len(p) == 0 or len(p) > 4:
                return "INVALID"
            if not all(c in '0123456789abcdefABCDEF' for c in p):
                return "INVALID"
        #нормализация IPv6 — убираем ведущие нули в каждом блоке
        normalized = ':'.join(f"{int(p, 16):x}" for p in parts)
        return f"IPv6 (нормализован: {normalized})"
    
    return "INVALID"


#основная часть пронграммы
inp = input("Введите IP-адрес: ")
print(check_ip(inp))
