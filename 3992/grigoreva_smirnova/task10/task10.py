def check_ip(addr):
    # проверка IPv4
    parts = addr.split('.')
    if len(parts) == 4:
        ipv4 = True
        for part in parts:
            if not part.isdigit() or int(part) < 0 or int(part) > 255:
                ipv4 = False
            if len(part) > 1 and part[0] == '0':
                ipv4 = False
        if ipv4:
            return "IPv4"
    
    # проверка IPv6
    if addr.startswith('[') and addr.endswith(']'):
        addr = addr[1:-1]
    
    parts = addr.split(':')
    if 3 <= len(parts) <= 8:
        ipv6 = True
        for part in parts:
            if part == "":
                continue
            if len(part) > 4:
                ipv6 = False
            for ch in part:
                if ch not in "0123456789abcdefABCDEF":
                    ipv6 = False
        if ipv6:
            return "IPv6"
    
    return "INVALID"

def normalize_ipv6(addr):
    if ':' not in addr:
        return addr
    
    if addr.startswith('[') and addr.endswith(']'):
        addr = addr[1:-1]
    
    parts = addr.split(':')
    result = []
    
    for part in parts:
        if part == "":
            result.append("")
        else:
            part = part.lstrip('0')
            result.append(part if part else "0")
    
    return ":".join(result)

# тест
ip = input("введите IP адрес: ")
result = check_ip(ip)
print(f"результат: {result}")

if result == "IPv6":
    print(f"нормализованный: {normalize_ipv6(ip)}")