import ipaddress


def check_ip(address):
    try:
        ip = ipaddress.ip_address(address)

        if isinstance(ip, ipaddress.IPv4Address):
            return "IPv4"

        if isinstance(ip, ipaddress.IPv6Address):
            return f"IPv6\nНормализованный: {ip.compressed}"

    except ValueError:
        return "INVALID"


address = input("Введите IP: ")

print(check_ip(address))