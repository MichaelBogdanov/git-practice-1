def check(s):
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or '([{'.index(stack[-1]) != ')]}'.index(c):
                return False
            stack.pop()
    return len(stack) == 0