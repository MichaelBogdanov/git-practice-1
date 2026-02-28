def prov(s):
    stack = []
    skobki = {')': '(', '}': '{', ']': '['}
    
    for i in s:
        if i in skobki.values():
            stack.append(i)
        elif i in skobki:
            if not stack or stack.pop() != skobki[i]:
                return False
    return True

print(prov("()[]{}")) 
print(prov(")("))