import ipaddress

def detect_ip_type(address: str) -> str:
    try:
        ip = ipaddress.IPv4Address(address)
        return "IPv4"
    except ipaddress.AddressValueError:
        pass

    try:
        ip = ipaddress.IPv6Address(address)
        normalized = ip.compressed
        print(f"Нормализованный IPv6: {normalized}")
        return "IPv6"
    except ipaddress.AddressValueError:
        return "INVALID"

ip_adress = "bruh"

result = detect_ip_type(ip_adress)
print(f"Этот адрес: {ip_adress} является: {result}")