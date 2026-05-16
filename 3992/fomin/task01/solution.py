def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        # Если это открывающая скобка, добавляем в стек
        if char in mapping.values():
            stack.append(char)
        # Если это закрывающая скобка
        elif char in mapping.keys():
            # Если стек пуст или последняя открытая скобка не совпадает с текущей закрывающей
            if not stack or mapping[char] != stack.pop():
                return False
                
    # Если стек пуст, все скобки закрыты верно
    return len(stack) == 0

if __name__ == "__main__":
    # Запрашиваем строку у пользователя
    user_input = input("Введите строку со скобками для проверки: ")
    
    result = "YES" if is_valid_parentheses(user_input) else "NO"
    print(f"Результат: {result}")