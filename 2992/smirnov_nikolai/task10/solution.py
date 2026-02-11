# Задача 10 — Проверка IP-адреса

import ipaddress

ip_str = input().strip()

try:
    ip = ipaddress.ip_address(ip_str)
    if isinstance(ip, ipaddress.IPv4Address):
        print("IPv4")
    else:
        print("IPv6")
        print(ip.compressed)  # нормализация IPv6
except ValueError:
    print("INVALID")
