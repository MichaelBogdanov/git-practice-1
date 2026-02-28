def function3():
    ip = input("Введите IP: ")
    
    if '.' in ip:
        parts = ip.split('.')
        if len(parts) == 4 and all(p.isdigit() for p in parts):
            return "Это V4"

    if ':' in ip:
        parts = ip.split(':')
        if len(parts) == 8:
            hex_chars = "0123456789abcdefABCDEF"
            if all(all(c in hex_chars for c in part) for part in parts):
                return "Это V6"
    return("INVALID")

print(function3())