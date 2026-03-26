
"""
Задача 1: Проверка корректности скобок
"""

def check_brackets(text):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    
    for char in text:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return "NO"
    
    return "YES" if not stack else "NO"

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = input()
    
    print(check_brackets(text))