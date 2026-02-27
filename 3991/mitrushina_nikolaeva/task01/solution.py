def is_valid_brackets(s):
    # Словарь соответствия открывающих и закрывающих скобок
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    # Стек для хранения открывающих скобок
    stack = []
    
    # Проходим по каждому символу в строке
    for char in s:
        # Если символ - открывающая скобка, добавляем в стек
        if char in brackets:
            stack.append(char)
        # Если символ - закрывающая скобка
        elif char in brackets.values():
            # Если стек пуст - закрывающая скобка без открывающей
            if not stack:
                return False
            # Проверяем, соответствует ли последняя открывающая скобка текущей закрывающей
            last_open = stack.pop()
            if brackets[last_open] != char:
                return False
    
    # В конце стек должен быть пустым
    return len(stack) == 0


# Версия с YES/NO для соответствия заданию
def check_brackets(s):
    return "YES" if is_valid_brackets(s) else "NO"


# Примеры использования
if __name__ == "__main__":
    test_strings = [
        "()",
        "()[]{}",
        "(]",
        "([{}])",
        "(((",
        "())",
        "hello (world) [test] {123}",
        "({[}])",
    ]
    
    for test in test_strings:
        result = check_brackets(test)
        print(f"'{test}' -> {result}")