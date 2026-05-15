# Задача 12: Разбор HTML-тегов

import re

def extract_tags(html):
    pattern = r'<(/?)([a-zA-Z][a-zA-Z0-9]*)[^>]*>'
    tags = re.findall(pattern, html)
    return [(slash, tag.lower()) for slash, tag in tags]

SELF_CLOSING = {'br', 'hr', 'img', 'input', 'meta', 'link'}

def check_html_tags(html):
    tags = extract_tags(html)
    stack = []
    
    for slash, tag in tags:
        if tag in SELF_CLOSING:
            continue
        
        if not slash:  # открывающий тег
            stack.append(tag)
        else:  # закрывающий тег
            if not stack:
                return False
            if stack[-1] != tag:
                return False
            stack.pop()
    
    return len(stack) == 0

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
        return None

print("=" * 50)
print("Задача 12: Разбор HTML-тегов")
print("=" * 50)

filename = input("Введите имя HTML-файла: ").strip()
html = read_file(filename)

if html:
    # Удаляем пробелы и переносы строк
    html = re.sub(r'\s+', ' ', html)
    
    result = check_html_tags(html)
    print(f"\nРезультат: {'VALID' if result else 'INVALID'}")
    
    # Дополнительные тесты
    print("\nДополнительные тесты:")
    tests = [
        ("<div><p></p></div>", True),
        ("<div><p></div></p>", False),
        ("<div><span></span></div>", True),
        ("<div><span></div>", False),
        ("<br>", True),
        ("<img src='a.jpg'/>", True),
    ]
    
    for test, expected in tests:
        result = check_html_tags(test)
        status = "✓" if result == expected else "✗"
        print(f"{status} {test} -> {'VALID' if result else 'INVALID'}")