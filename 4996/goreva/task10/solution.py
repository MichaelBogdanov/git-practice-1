def check(ip):
    if '.' in ip:
        str = ip.split('.')
        if len(str) != 4:
            return 'INVALID'
        cap = 255
        for i in str:
            try:
                if int(i, 10) > cap or int(i, 10) < 0:
                    return 'INVALID'
            except ValueError:
                return 'INVALID'
        return 'IPv4'
    elif ':' in ip:
        str = ip.split(':')
        if len(str) != 8:
            return 'INVALID'
        cap = int('ffff', 16)
        for i in str:
            try:
                if int(i, 16) > cap or int(i, 16) < 0:
                    return 'INVALID'
            except ValueError:
                return 'INVALID'
        return 'IPv6'
    else:
        return 'INVALID'

print(check(input()))