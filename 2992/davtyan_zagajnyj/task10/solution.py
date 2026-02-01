import ipaddress

s = input("Введите IP-адрес: ").strip()
try:
    ip = ipaddress.ip_address(s)
    print("IPv4" if ip.version == 4 else "IPv6")
except ValueError:
    print("INVALID")