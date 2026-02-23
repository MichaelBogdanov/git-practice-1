s = input().strip()
res = "Invalid"

parts = s.split('.')
if len(parts) == 4:
    ok = True
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            ok = False
            break
    if ok:
        res = "IPv4"

if res == "Invalid":
    if s.count('::') > 1:
        pass
    elif '::' in s:
        left, right = s.split('::', 1)
        left_parts = left.split(':') if left else []
        right_parts = right.split(':') if right else []
        total_parts = len(left_parts) + len(right_parts)
        if total_parts <= 7:
            ok = True
            for p in left_parts + right_parts:
                if len(p) == 0 or len(p) > 4:
                    ok = False
                    break
                try:
                    int(p, 16)
                except ValueError:
                    ok = False
                    break
            if ok:
                res = "IPv6"
    else:
        parts = s.split(':')
        if len(parts) == 8:
            ok = True
            for p in parts:
                if len(p) == 0 or len(p) > 4:
                    ok = False
                    break
                try:
                    int(p, 16)
                except ValueError:
                    ok = False
                    break
            if ok:
                res = "IPv6"

print(res)
