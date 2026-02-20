import sys

def check_brackets(text):
    """
    Проверяет правильность закрытия скобок в строке
    """
    # Соответствие открывающих и закрывающих скобок
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    # Множество открывающих скобок для быстрой проверки
    opening_brackets = set(brackets.keys())
    # Множество закрывающих скобок
    closing_brackets = set(brackets.values())
    
    # Стек для хранения открывающих скобок
    stack = []
    
    for char in text:
        if char in opening_brackets:
            # Если встретили открывающую скобку, добавляем в стек
            stack.append(char)
        elif char in closing_brackets:
            # Если встретили закрывающую скобку
            if not stack:
                # Стек пуст - закрывающая скобка без открывающей
                return False
            
            # Проверяем, соответствует ли последняя открывающая скобка текущей закрывающей
            last_opening = stack.pop()
            if brackets[last_opening] != char:
                # Несоответствие типов скобок
                return False
    
    # В конце стек должен быть пустым
    return len(stack) == 0


if __name__ == "__main__":
    # Читаем имя файла из аргументов командной строки
    if len(sys.argv) != 2:
        print("Использование: python solution.py input.txt")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().strip()
        
        result = check_brackets(text)
        print("yes" if result else "no")
        
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        sys.exit(1)