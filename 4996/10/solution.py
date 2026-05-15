# Задача 10: Проверка IP-адреса (IPv4 и IPv6)

def is_valid_ipv4(ip):
    parts = ip.split('.')
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part or (len(part) > 1 and part[0] == '0'):
            return False
        
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    
    return True

def is_valid_ipv6(ip):
    if '::' in ip:
        if ip.count('::') > 1:
            return False
        
        left, right = ip.split('::')
        left_parts = left.split(':') if left else []
        right_parts = right.split(':') if right else []
        
        if len(left_parts) + len(right_parts) > 8:
            return False
        
        missing = 8 - (len(left_parts) + len(right_parts))
        parts = left_parts + ['0'] * missing + right_parts
    else:
        parts = ip.split(':')
    
    if len(parts) != 8:
        return False
    
    for part in parts:
        if not part:
            return False
        try:
            num = int(part, 16)
            if num < 0 or num > 65535:
                return False
            if len(part) > 4:
                return False
        except ValueError:
            return False
    
    return True

def check_ip(ip):
    if is_valid_ipv4(ip):
        return "IPv4"
    elif is_valid_ipv6(ip):
        return "IPv6"
    else:
        return "INVALID"

print("=" * 50)
print("Задача 10: Проверка IP-адреса")
print("=" * 50)

# Тесты
test_ips = [
    "192.168.1.1",
    "255.255.255.255",
    "0.0.0.0",
    "256.1.1.1",
    "192.168.1",
    "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "2001:db8:85a3::8a2e:370:7334",
    "::1",
    "::",
    "not-an-ip"
]

print("Тестирование:")
print("-" * 50)
for ip in test_ips:
    ip_type = check_ip(ip)
    print(f"{ip:45} -> {ip_type}")

# Интерактивный режим
print("\n" + "=" * 50)
print("Интерактивный режим (введите 'exit' для выхода)")

while True:
    ip = input("\nВведите IP-адрес: ").strip()
    if ip.lower() == 'exit':
        break
    
    ip_type = check_ip(ip)
    print(f"Тип: {ip_type}")