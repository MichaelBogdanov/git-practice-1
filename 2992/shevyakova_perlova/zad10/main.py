
import sys
import re

ip = sys.argv[1].strip()

def is_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not (part.isdigit() and 0 <= int(part) <= 255):
            return False
    return True

def is_ipv6(ip):
    hex_digits = '0123456789abcdefABCDEF'
    if ':' not in ip or ip.count('::') > 1:
        return False
    
    parts = ip.split(':')
    if len(parts) < 2 or len(parts) > 8:
        return False
    
    for part in parts:
        if part == '':
            continue
        if len(part) > 4:
            return False
        for char in part:
            if char not in hex_digits:
                return False
    return True

if is_ipv4(ip):
    print("IPv4")
elif is_ipv6(ip):
    print("IPv6")
else:
    print("INVALID")
