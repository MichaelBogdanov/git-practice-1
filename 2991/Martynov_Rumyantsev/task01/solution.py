text = input("Введите строку со скобками: ")


stack = []

for symbol in text:
    if symbol == '(' or symbol == '[' or symbol == '{':
        stack.append(symbol)
    
    elif symbol == ')':
        if len(stack) == 0 or stack[-1] != '(':
            print("NO")
            exit()
        stack.pop()
    
    elif symbol == ']':
        if len(stack) == 0 or stack[-1] != '[':
            print("NO")
            exit()
        stack.pop()
    
    elif symbol == '}':
        if len(stack) == 0 or stack[-1] != '{':
            print("NO")
            exit()
        stack.pop()

if len(stack) == 0:
    print("YES")
else:
    print("NO")