import ipaddress

def classify_ip(ip: str) -> str:
    ip = ip.strip()

    try:
        ipaddress.IPv4Address(ip)
        return "IPv4"
    except ipaddress.AddressValueError:
        pass

    try:
        ipaddress.IPv6Address(ip)
        return "IPv6"
    except ipaddress.AddressValueError:
        pass

    return "INVALID"

def normalize_ipv6(ip: str) -> str:
    try:
        addr = ipaddress.IPv6Address(ip)
        return str(addr.compressed)
    except ipaddress.AddressValueError:
        return "INVALID"

if __name__ == "__main__":
    ip = input("Введите IP‑адрес: ").strip()

    kind = classify_ip(ip)
    print("Тип:", kind)

    if kind == "IPv6":
        print("Нормализованный IPv6:", normalize_ipv6(ip))

# 192.168.0.1
# 2001:0db8:0000:0000:0000:ff00:0042:8329