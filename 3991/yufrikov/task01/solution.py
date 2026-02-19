def check_brackets(text):
    stack = [] # стек для скобок
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in text:
        if char in '([{':
            stack.append(char) # добавлем в стек
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]: # проверка последнего символа в стеке
                return "NO"
            stack.pop()
    
    return "YES" if not stack else "NO"

# print(check_brackets("({[]})"))
# print(check_brackets("({[})"))