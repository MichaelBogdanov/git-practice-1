import sys
import ipaddress

def check_ip(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
        return "IPv4" if isinstance(ip, ipaddress.IPv4Address) else "IPv6"
    except ValueError:
        return "INVALID"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python solution.py <IP>")
        sys.exit(1)
    print(check_ip(sys.argv[1]))