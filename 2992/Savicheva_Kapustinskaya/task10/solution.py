def normalize_ipv6(address):
    # разделяем на части, убираем ведущие нули в каждой группе
    parts = address.split(':')
    normalized_parts = [part.lstrip('0') if part.lstrip('0') != '' else '0' for part in parts]
    return ':'.join(normalized_parts)

def validate_ip(ip):
    # проверка на IPv4
    if '.' in ip:
        parts = ip.split('.')
        if len(parts) == 4:
            for part in parts:
                if not part.isdigit() or not (0 <= int(part) <= 255):
                    return "INVALID"
                if len(part) > 1 and part[0] == '0':  # ведущие нули в IPv4 запрещены
                    return "INVALID"
            return "IPv4"

    # проверка на IPv6
    if ':' in ip:
        parts = ip.split(':')
        if len(parts) == 8:
            for part in parts:
                if not (1 <= len(part) <= 4):
                    return "INVALID"
                try:
                    int(part, 16)  # проверка, что это шестнадцатеричное число
                except ValueError:
                    return "INVALID"
            return f"IPv6 (Normalized: {normalize_ipv6(ip)})"

    return "INVALID"

if __name__ == "__main__":
    user_ip = input("Введите IP-адрес: ").strip()
    print(validate_ip(user_ip))