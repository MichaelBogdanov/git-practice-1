def is_ipv4(s: str) -> bool:
    parts = s.split(".")

    if len(parts) != 4:
        return False
    
    for p in parts:
        if p == "" or not p.isdigit():
            return False
        
        if len(p) > 1 and p[0] == "0":
            return False
        
        n = int(p)

        if n < 0 or n > 255:
            return False
    return True


def is_ipv6(s: str) -> bool:
    parts = s.split(":")

    if len(parts) != 8:
        return False
    
    hexdigits = set("0123456789abcdefABCDEF")

    for p in parts:
        if not (1 <= len(p) <= 4):
            return False
        
        if any(ch not in hexdigits for ch in p):
            return False
    return True


addr = input().strip()

if is_ipv4(addr):
    print("IPv4")
elif is_ipv6(addr):
    print("IPv6")
else:
    print("INVALID")


'''
    192.168.0.1 - v4
    2001:0db8:85a3:0000:0000:8a2e:0370:7334 - v6
    256.10.10.10 - inv
'''
