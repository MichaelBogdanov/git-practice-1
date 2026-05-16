# проверка IP-адреса
import sys


def check_ip(ip):
    parts = ip.split('.')
    if len(parts) == 4:
        ok = True
        for p in parts:
            if not p.isdigit():
                ok = False
                break
            num = int(p)
            if num < 0 or num > 255 or (len(p) > 1 and p[0] == '0'):
                ok = False
                break
        if ok:
            return "IPv4"

    parts = ip.split(':')
    if len(parts) == 8:
        ok = True
        for p in parts:
            if len(p) == 0 or len(p) > 4:
                ok = False
                break
            for c in p:
                if not (c.isdigit() or ('a' <= c.lower() <= 'f')):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return "IPv6"

    return "INVALID"


def normalize_ipv6(ip):
    parts = ip.split(':')
    norm = []
    for p in parts:
        norm.append(p.lower().lstrip('0') or '0')
    return ':'.join(norm)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python solution.py <ip-адрес>")
    else:
        result = check_ip(sys.argv[1])
        print(result)
        if result == "IPv6":
            print("Нормализованный:", normalize_ipv6(sys.argv[1]))
