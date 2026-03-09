def check(str):
    open = {
    ')' : '(',
    '}' : '{',
    ']' : '[',
    }

    str1 = []

    for c in str:
        if c in '({[':
            str1.append(c)
        elif c in ')}]':
            if not str1 or open[c] != str1[-1]:
                return False      
            str1.pop()

    return len(str1) == 0

print(check(input()))